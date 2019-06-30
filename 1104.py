# coding: utf-8
""" 1104. 分糖果
排排坐，分糖果。
我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。
给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。
然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。
重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。
返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

示例 1：
输入：candies = 7, num_people = 4
输出：[1,2,3,1]

示例 2：
输入：candies = 10, num_people = 3
输出：[5,2,3]
"""


class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        i = 0
        round = -1
        result = [0] * num_people
        while candies > 0:
            if i == 0:
                round += 1
            dispatch = round * num_people + i + 1
            result[i] += dispatch if dispatch < candies else candies
            i = (i+1) % num_people
            candies -= dispatch
        return result


if __name__ == '__main__':
    s = Solution()
    candies = 7
    num_people = 4
    print(s.distributeCandies(candies, num_people))
