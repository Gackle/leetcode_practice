# coding: utf-8
""" 621. 任务调度器
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

提示：discuss 里有一个直接计算套用公式，和这个其实类似
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        d = dict()
        for task in tasks:
            d[task] = d.get(task, 0) + 1
        keys = sorted(d, key=lambda x: d[x], reverse=True)
        # 只有一类任务
        if len(keys) == 1:
            return d[keys[0]]*(n+1)-n
        # 如果 n 为 0，表示无间隔执行：
        if n == 0:
            return len(tasks)
        if n > len(keys)-1:
            # 1. n 的值比 key 的总和要大1以上，需要待命填充，则最多任务类型为准;如果有多个最多，则累加1
            left = 0
            for i in keys[1:]:
                if d[i] == d[keys[0]]:
                    left += 1
            return d[keys[0]]*(n+1)-n+left
        else:
            # 2. n 的值比 key 的总和-1要小或等于，不需要填充
            left = 0
            for i in keys[1:]:
                if d[i] == d[keys[0]]:
                    left += 1
            return max(d[keys[0]]*(n+1)-n+left, len(tasks))


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B", "C"]
    n = 2
    s = Solution()
    print(s.leastInterval(tasks, n))
