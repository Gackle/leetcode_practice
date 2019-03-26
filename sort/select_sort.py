# coding: utf-8
''' 选择排序
'''


def select_sort(l):
    '''
    :type l:    List[int]
    :rtype:     List[int]
    '''
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

    return l


if __name__ == '__main__':
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(select_sort(l))
