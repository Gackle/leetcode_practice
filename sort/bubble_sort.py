# coding: utf-8
def bubble_sort(l):
    '''
    :type l:    List[int]
    :rtype:     List[int]

    冒泡排序
    '''
    flag = False
    for i in range(len(l)):
        flag = False
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                flag = True
        if not flag:
            break

    return l


if __name__ == '__main__':
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(bubble_sort(l))
