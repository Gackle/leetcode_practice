# coding: utf-8
""" 40. 组合总和Ⅱ
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

提示：回溯
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 想了很久也没想到，如何在不排序的情况下去重 [2, 6] 跟  [6, 2] 的情况
        # 配合下面“一层递归不出现两次”来使用
        candidates.sort(reverse=1)
        length = len(candidates)
        return(self.dfs(0, length, target, candidates))

    def dfs(self, start, end, target, candidates):
        return_data = list()
        for i in range(start, end):
            cur = candidates[i]
            if cur > target:
                continue
            if i > start and candidates[i] == candidates[i-1]:
                # 同一层递归，如果已经出现过则跳过
                # 除非出现在下一层的开头，纳入处理范围
                continue
            if cur == target:
                return_data.append([cur])
            else:
                nt = target - cur
                out = self.dfs(i+1, end, nt, candidates)
                for i in out:
                    i.append(cur)
                return_data.extend(out)
        return return_data


if __name__ == "__main__":
    s = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))
