# coding: utf-8
""" 464. 我能赢吗
给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），
判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：
输入：
maxChoosableInteger = 10
desiredTotal = 11
输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

提示：动态规划 极大极小化

这条题，认真想了两天，还是不会
关键点在于：如果下一个状态存在必败，则上一个状态必胜；用 32 位整数替代 0-20 数值范围作为状态值
"""


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.max_num = maxChoosableInteger
        # 如果总和比目标值还要小或者等于，先手必败
        if (maxChoosableInteger+1)*maxChoosableInteger/2 <= desiredTotal or desiredTotal < 0:
            return False
        # 可选值比目标值还要大，先手必胜
        if maxChoosableInteger >= desiredTotal:
            return True
        # 用于状态压缩
        self.d = dict()
        return self.dfs(desiredTotal, 0)

    def dfs(self, total, choose):
        """ 深度搜索
        :type total: int
        :type choose: int
        """
        if total <= 0:
            return False
        if choose in self.d:
            return self.d[choose]

        for i in range(1, self.max_num+1):
            if (choose ^ (1 << i)) < choose:
                # 已选择过位异或会缩小
                continue
            next_choose = choose | (1 << i)
            if not self.dfs(total-i, next_choose):
                self.d[choose] = True
                return True
        self.d[choose] = False
        return False


class SolutionError(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.matrix = dict()
        self.max_num = maxChoosableInteger
        # 如果总和比目标值还要小或者等于，先手必败
        if (maxChoosableInteger+1)*maxChoosableInteger/2 <= desiredTotal:
            return False
        # 可选值比目标值还要大，先手必胜
        if maxChoosableInteger >= desiredTotal:
            return True

        # 依然需要深度搜索
        always_win = False
        for i in range(1, maxChoosableInteger+1):
            result = self.dfs(1 << i, desiredTotal-i)
            # 只要先手选了任何一个数字，其下个结果都必败，则先手必胜
            if result != 1:
                always_win = True
        return always_win

    def dfs(self, choose, target):
        """
        :type choose: int
        :type target: int
        :rtype: int
        """
        return_data = 0
        for i in range(1, self.max_num+1)[::-1]:
            # 先判断是否可选取
            if choose ^ (2**i) < choose:
                continue
            # 更新状态
            next_choose = choose ^ (2**i)
            # 搜索状态表，减少遍历次数
            if next_choose in self.matrix:
                return self.matrix[next_choose]
            # 如果大于剩余值，返回胜利
            if i >= target:
                self.matrix[choose] = 1
                return 1
            else:
                next_target = target - i
                result = self.dfs(next_choose, next_target)
                # 由于下一个状态为必胜，所以当前状态为必输，在递归中已记录在 dict 中
                if result != 1:
                    return_data = 1
                    break
        # self.matrix(choose)
        self.matrix[choose] = return_data
        return return_data


if __name__ == "__main__":
    s = Solution()
    maxChoosableInteger = 20
    desiredTotal = 209
    print(s.canIWin(maxChoosableInteger, desiredTotal))
