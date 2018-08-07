# coding: utf-8
""" 675. 为高尔夫比赛砍树

你被请来给一个要举办高尔夫比赛的树林砍树. 树林由一个非负的二维数组表示， 在这个数组中：

0 表示障碍，无法触碰到.
1 表示可以行走的地面.
比1大的数 表示一颗允许走过的树的高度.
你被要求按照树的高度从低向高砍掉所有的树，每砍过一颗树，树的高度变为1。

你将从（0，0）点开始工作，你应该返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且至少有一颗树需要你砍。

示例 1:

    输入:
    [
        [1,2,3],
        [0,0,4],
        [7,6,5]
    ]
    输出: 6
"""


class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        import Queue
        if len(forest) < 0 or len(forest[0]) < 0:
            return 0
        # BFS 队列
        queue = Queue.PriorityQueue()
        queue.put((forest[0][0], (0, 0)))
        # 遍历方向
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        step = 0
        # 已砍掉的树木的个数
        count_for_cut_off = 1
        # 无法通行的个数
        count_for_zero = sum([row.count(0) for row in forest])
        # 需要砍掉的树的个数
        count_should_cutoff = len(forest) * len(forest[0]) - count_for_zero
        while len(queue) > 0:
            node = queue.get(0)
            if count_for_cut_off == count_should_cutoff:
                return step
            for direction in directions:
                row = node[0] - direction[0]
                column = node[1] - direction[1]
                # 越界判断
                if row < 0 or row > len(forest) - 1 or column < 0 or column > len(forest[0]) - 1:
                    continue
                next_node = forest[row][column]
                # 障碍物判断
                if next_node == 0:
                    continue
                # 是否已经访问过
                if next_node == 1:
                    continue
                queue.append((row, column))
            step += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    forest = [
        [1, 2, 3],
        [0, 0, 4],
        [7, 6, 5]
    ]
    print(s.cutOffTree(forest))
