# coding: utf-8
""" 1052. 爱生气的书店老板  显示英文描述  我的提交返回竞赛
用户通过次数 37
用户尝试次数 50
通过次数 37
提交次数 63
题目难度 Medium
今天，书店老板有一家店打算试营业 customers.length 分钟。
每分钟都有一些顾客（customers[i]）进入书店，所有这些顾客都会在那一分钟结束后离开。
在某些时候，书店老板会生气。
如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
当书店老板生气时，那一分钟的顾客就会不满意，否则他们是满意的。

书店老板知道一个秘密技巧，可以让自己连续 X 分钟不生气，但只能使用一次。
返回全天感到满意的最大客户数量。

示例：
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16

解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

提示：
1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1

思路：
应该寻找这样一个子区间，其大小为 X，同时区间内 grumpy 为 0 的 customer 的数目最大
为了加快速度，可以使用双指针头尾指向
"""


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        n = len(customers)
        if X <= 0:
            return sum([customers[i] for i in range(n) if grumpy[i] == 0])
        if X >= n:
            return sum(customers)
        # 双指针法
        max_get = sum([customers[i] for i in range(X) if grumpy[i] == 1])
        cur = max_get
        i = 0
        j = X - 1
        while j < n-1:
            cur -= customers[i] if grumpy[i] == 1 else 0
            i += 1
            j += 1
            cur += customers[j] if grumpy[j] == 1 else 0
            if cur > max_get:
                max_get = cur

        return sum([customers[i] for i in range(n) if grumpy[i] == 0]) + max_get


if __name__ == '__main__':
    s = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # customers = [1]
    # customers = [4, 10, 10]
    # customers = [10, 1, 7]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # grumpy = [0]
    # grumpy = [1, 1, 0]
    # grumpy = [0, 0, 0]
    x = 3
    # x = 1
    # x = 2
    # x = 2
    print(s.maxSatisfied(customers, grumpy, x))
