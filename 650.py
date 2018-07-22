# coding: utf-8
''' 650. 只有两个键的键盘
'''


class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        min_steps_list = []
        for i in range(n + 1):
            if i < 2:
                min_steps_list.append(0)
            else:
                min_steps_list.append(i)
                j = 2
                while j < sqrt(i):
                    if not (i % j):
                        min_steps_list[i] = min(min_steps_list[i], min_steps_list[j] + (i // j))
                        min_steps_list[i] = min(min_steps_list[i], min_steps_list[i // j] + j)
                    j += 1
        return min_steps_list[n]


if __name__ == '__main__':
    s = Solution()
    print(s.minSteps(100 - 1))
