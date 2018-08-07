# coding: utf-8
""" 204. 计数质数

统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        nums = [1] * n
        nums[0] = 0
        nums[1] = 0
        count = n - 2
        pows = 2
        for i in range(2, len(nums)):
            if nums[i] == 0:
                continue
            pows = 2
            p = pows * i
            while p < n:
                if nums[p]:
                    nums[p] = 0
                    count -= 1
                pows += 1
                p = pows * i
        return count


class Solution2:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1] * n

        prime[0] = prime[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])

        return sum(prime)


if __name__ == "__main__":
    s = Solution2()
    print(s.countPrimes(499979))
    # print(s.countPrimes(10))
