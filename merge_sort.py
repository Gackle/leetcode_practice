# coding: utf-8
''' 归并排序
'''


def merge_sort(l):
    '''
    :type l: List[int]
    :rtype : List[int]
    '''
    if len(l) == 0 or len(l) == 1:
        return l
    elif len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return [l[0], l[1]]
    else:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    '''
    :type left: List[int]
    :type right: List[int]
    :rtype : List[int]

    合并列表
    '''
    data = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            data.append(left[l_index])
            l_index += 1
        else:
            data.append(right[r_index])
            r_index += 1

    if l_index < len(left):
        data += left[l_index:]
    else:
        data += right[r_index:]

    return data


if __name__ == '__main__':
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(merge_sort(l))
