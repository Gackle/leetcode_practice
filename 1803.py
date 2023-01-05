# encoding: utf-8
"""1803. 统计异或值在范围内的数对有多少
给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[j]) <= high 。

示例一：
输入：nums = [1,4,2,7], low = 2, high = 6
输出：6

示例二：
输入：nums = [9,8,4,2,1], low = 5, high = 14
输出：8
"""
from typing import List

HIGH_BIT = 14


class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.sum = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num: int) -> None:
        cur = self.root
        # 从高位到低位倒序
        # 将一个数字转为二进制的形式插入到 trie 中，trie 的每个节点最多只有两个子节点，sum 表示二进制前缀相同的数字当前有多少个
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
            cur.sum += 1

    def get(self, num: int, x: int) -> int:
        res = 0
        cur = self.root
        # 从高位到低位倒序
        for k in range(HIGH_BIT, -1, -1):
            bit = (num >> k) & 1
            if (x >> k) & 1:
                if cur.children[bit]:  # 如果有和自己当前位相同子节点的走法，那么能保证前缀一定比 1 小，所以他的 sum 代表了有多少个匹对的数字满足这个前缀比 x 小的，累加 sum
                    res += cur.children[bit].sum
                if not cur.children[bit ^ 1]:  # 与 1 异或，即往反方向的子节点走，如果不能走则返回（剪枝），能走的话同时满足了前缀相同（因为从 (x >> k) & 1 == 1）保证了走法只能相同或者比 1 小；
                    return res
                cur = cur.children[bit ^ 1]
            else:  # (x >> k) & 1 == 0，那么要和自己当前位相同子节点的走法才能保证前缀相同：任何数字和自身异或都为 0 ；如果不能走就返回（剪枝）
                if not cur.children[bit]:
                    return res
                cur = cur.children[bit]
        # 边界处理：如果能完整走完整棵树，说明 num 的异或结果刚好和 x 相同，根据题意也满足条件，所以要补充最后叶子节点的 sum
        res += cur.sum
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def f(nums: List[int], x: int) -> int:
            res = 0
            trie = Trie()
            # 遍历过程：从第二个开始，每次都先把他的前一个插入到 trie ，然后把数字和当前 trie 中有的数字进行匹对，看是否小于等于 x
            for i in range(1, len(nums)):
                trie.add(nums[i - 1])
                res += trie.get(nums[i], x)
            return res
        return f(nums, high) - f(nums, low - 1)


if __name__ == "__main__":
    nums = [9, 8, 4, 2, 1]
    low = 5
    high = 14
    s = Solution()
    a = s.countPairs(nums=nums, low=low, high=high)
    print(a)
