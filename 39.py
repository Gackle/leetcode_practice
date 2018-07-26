# coding: utf-8
''' 39. 组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

- 所有数字（包括 target）都是正整数。
- 解集不能包含重复的组合。
'''


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == [] or candidates is None:
            return []
        self.returnList = []
        n = len(candidates)
        for index in range(n):
            self.recursiveSearch(candidates, index, target - candidates[index], [candidates[index]])
        return self.returnList

    def recursiveSearch(self, candidates, start, target, current):
        """
        :type candidates: List[int]
        :type start: int
        :type target: int
        :type curent: List[int]
        """
        if target == 0:
            self.returnList.append(current[:])
        elif target < 0:
            return
        else:
            n = len(candidates)
            for index in range(start, n):
                current.append(candidates[index])
                self.recursiveSearch(candidates, index, target - candidates[index], current)
                current.pop()


if __name__ == '__main__':
    s = Solution()
    # candidates = [2, 3, 6, 7]
    candidates = [2, 3, 5]
    target = 8
    print(s.combinationSum(candidates, target))
