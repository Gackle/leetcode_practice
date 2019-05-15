# coding: utf-8
from functools import partial
import time
import random
shuffle_n = partial(random.shuffle, random=None)


def build_n(n: int, max_int: int = 10000000) -> list:
    data = list()
    for i in range(n):
        data.append(random.randint(0, max_int))
    return data


class Solution(object):
    def __init__(self, data):
        self.data = data

    def partition(self, top_n: int) -> list:
        """ 分治法，需要较大的空间，时间复杂度为 O(n) (n为数据集大小)
        """
        result = list()

        def _partition(l: list, n: int):
            bench = l[0]
            lt = list()
            gt = list()
            for i in l[1:]:
                if i < bench:
                    lt.append(i)
                else:
                    gt.append(i)
            # 判断 gt 和 n 的大小
            gt.append(bench)
            if len(gt) > n:
                _partition(gt, n)
            elif len(gt) < n:
                result.extend(gt)
                _partition(lt, n-len(gt))
            else:
                result.extend(gt)
            return
        _partition(self.data, top_n)
        return result

    def min_heap(self, top_n: int) -> list:
        """ 最小堆法，时间复杂度为 O(nlogn)
        """
        import heapq
        heap = self.data[:top_n][:]
        heapq.heapify(heap)
        for i in self.data[top_n:]:
            if i < heap[0]:
                continue
            else:
                heapq.heappush(heap, i)
        return heap


if __name__ == '__main__':
    n = 1000000
    top_n = 5
    data = build_n(n, 1200000)
    so = Solution(data)
    # 常规排序求前 top_N 个值
    s = time.time()
    data.sort(reverse=True)
    e = time.time()
    print(data[:top_n], e-s)
    # top N 算法
    s = time.time()
    result = so.min_heap(top_n)
    e = time.time()
    print(result, e-s)
    # top N 算法
    s = time.time()
    result = so.partition(top_n)
    e = time.time()
    print(result, e-s)
