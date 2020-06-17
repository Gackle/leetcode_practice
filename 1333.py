# -*- coding: utf-8 -*-
""" 1333. 餐厅过滤器
给你一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。
你必须使用以下三个过滤器来过滤这些餐馆信息。
其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，
为 false 则意味着可以包括任何餐馆。
此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。

过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。
简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。
"""
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # 练手题？过滤后插入排序（最直观） - id 并不是从小到大默认的
        # 当然最快是利用自带的 sorted 方法进行排序，不是自己做排序
        result = []
        for r in restaurants:
            if veganFriendly == 1 and r[2] == 0:
                continue
            if r[3] > maxPrice or r[4] > maxDistance:
                continue
            if not result:
                result.append(r[:2])
            else:
                flag = False
                for i, v in enumerate(result):
                    if r[1] > v[1] or (r[1] == v[1] and r[0] > v[0]):
                        result = result[:i] + [r[:2]] + result[i:]
                        flag = True
                        break
                    elif r[1] == v[1] and r[0] < v[0]:
                        flag = True
                        result = result[:i+1] + [r[:2]] + result[i+1:]
                        break
                if not flag:
                    result.append(r[:2])
        return [x[0] for x in result]


if __name__ == "__main__":
    s = Solution()
    # case 1 -  [3, 1, 5]
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
        3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 1
    maxPrice = 50
    maxDistance = 10
    print(s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
    assert s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance) == [3, 1, 5], 'case 1 wrong'
    # case 2 - [4, 3, 2, 1, 5]
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
        3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 0
    maxPrice = 50
    maxDistance = 10
    print(s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
    assert s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance) == [4, 3, 2, 1, 5], 'case 2 wrong'
    # case 3 - [4, 5]
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
        3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 0
    maxPrice = 30
    maxDistance = 3
    print(s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
    assert s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance) == [4, 5], 'case 3 wrong'
