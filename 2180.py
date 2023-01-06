# encoding: utf-8
""" 2180. 统计各位数字之和为偶数的整数个数

给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。
正整数的 `各位数字之和` 是其所有位上的对应数字相加的结果。

示例一：
输入：num = 4
输出：2

示例二：
输入：num = 30
输出：14

"""
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            odd = 0
            while i // 10:
                s = i % 10
                i = i // 10
                if s % 2:
                    odd += 1
            odd += (i % 10) % 2
            count += 0 if (odd % 2) else 1
        return count


if __name__ == "__main__":
    s = Solution()
    num = 30
    print(s.countEven(num))
