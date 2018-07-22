# coding: utf-8
'''
使用标准库提供的 heapq 实现堆排序
'''
import heapq


def heap_sort(l):
    '''
    :type l:    List[int]
    :rtype:     List[int]

    使用标准库 heapq 实现堆排序
    '''
    ret_list = []
    for value in l:
        heapq.heappush(ret_list, value)

    return [heapq.heappop(ret_list) for x in range(len(ret_list))]


if __name__ == "__main__":
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(heap_sort(l))
