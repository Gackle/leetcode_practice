# encoding: utf-8
"""2475. 数组中不等三元组的数目
给你一个下标从 0 开始的正整数数组 nums 。请你找出并统计满足下述条件的三元组 (i, j, k) 的数目：
0 <= i < j < k < nums.length
nums[i]、nums[j] 和 nums[k] 两两不同 。
换句话说：nums[i] != nums[j]、nums[i] != nums[k] 且 nums[j] != nums[k] 。
返回满足上述条件三元组的数目。
 

示例 1：
输入：nums = [4,4,2,4,3]
输出：3
解释：下面列出的三元组均满足题目条件：
- (0, 2, 4) 因为 4 != 2 != 3
- (1, 2, 4) 因为 4 != 2 != 3
- (2, 3, 4) 因为 2 != 4 != 3
共计 3 个三元组，返回 3 。
注意 (2, 0, 4) 不是有效的三元组，因为 2 > 0 。
示例 2：
输入：nums = [1,1,1,1,1]
输出：0
解释：不存在满足条件的三元组，所以返回 0 。
 

提示：
3 <= nums.length <= 100
1 <= nums[i] <= 1000
"""
from typing import List
from functools import reduce
from itertools import combinations
from collections import Counter
class Solution:
    def unequalTripletsSlow(self, nums: List[int]) -> int:
        hmap = dict()
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
        # print(hmap)
        keys = hmap.keys()
        if len(keys) < 3:
            return 0
        res = 0
        combine = combinations(keys, 3)
        for lst in combine:
            res += reduce(lambda x, y: x * y, [hmap[i] for i in lst])
        # 去掉 reduce 可以加速 5 倍
        # for a, b, c in combine:
        #     res += hmap[a] * hmap[b] * hmap[c]
        return res
    
    def unequalTripletsUpdate(self, nums: List[int]) -> int:
        # 使用 Counter 节省开支
        cnt = Counter(nums)
        ans = 0
        for a,b,c in combinations(set(nums),3):
            ans += cnt[a] * cnt[b] * cnt[c]
        return ans
    
    def unequalTriplets(self, nums: List[int]) -> int:
        # 在x之前遍历过的数有a个，（当前遍历的）等于x的数有b个，在x之后遍历过的数有c个
        ans, a, c = 0, 0, len(nums)
        for b in Counter(nums).values():
            c -= b
            ans += a * b * c
            a += b
        return ans

    

if __name__ == '__main__':
    s = Solution()
    examples = [
        ([4,4,2,4,3], 3),
        ([1,1,1,1,1], 0),
        ([1,3,1,2,4], 7)
    ]
    for row in examples:
        nums, ans = row
        res = s.unequalTriplets(nums)
        assert res == ans, f"unequalTriplets({nums}) except {ans} but got {res}"
    
    print("You Pass!")