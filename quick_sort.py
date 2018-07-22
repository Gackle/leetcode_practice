# coding: utf-8
''' 快速排序
'''


def quick_sort(l):
    '''
    :type l: List[int]
    :rtype: List[int]
    '''
    if len(l) == 0 or len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return [l[0], l[1]]
    elif len(l) > 2:
        left = []
        right = []
        for i in l[1:]:
            if i > l[0]:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [l[0]] + quick_sort(right)


if __name__ == "__main__":
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(quick_sort(l))
