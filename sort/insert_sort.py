# coding: utf-8
''' 插入排序
'''


def insert_sort(l):
    '''
    :type l:    List[int]
    :rtype:     List[int]
    '''
    for i in range(1, len(l)):
        j = i
        while j - 1 >= 0:
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
    return l


if __name__ == '__main__':
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(insert_sort(l))
