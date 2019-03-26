# coding: utf-8
'''
堆排序的基本思路：

堆排序实际上是选择排序的变种，因为利用了堆是一棵完全二叉树的特性来使得内循环的查询可以变为 O(logn)，
所以总的时间复杂度为 O(nlogn)

1. 建立初始堆（大顶堆或小顶堆）
2. 取堆顶元素
3. 将堆的最后一个元素提到堆顶，然后和左右子节点对比，“节点下沉”，恢复为大顶堆/小顶堆
4. 重复第 2 ~ 3 步，直到堆中的元素消耗完毕

P.S. 建堆操作：从最后一个非叶子节点开始做“节点下沉”，一直到堆顶
最后一个非叶子节点公式: index = n / 2 - 1, n 为元素个数，index 为从 0 开始最后一个非叶子节点的下标

'''


def heap_sort(l):
    '''
    :type l:    List[int]

    堆排序
    '''
    # 最后返回的排列完的堆（数组）
    ret_list = []

    if l == []:
        return ret_list

    # 从最后一个非叶子节点开始调整堆，其实这里也需要时间消耗，为 O(n/2 * logn)，但实际上大头还在后面
    # 也正因为如此，堆排序适合大量元素排序，这样的话建堆操作的时间占比才会更小
    for i in range(len(l) // 2)[::-1]:
        shift_heap(l, i, len(l) - 1)
        # shift_heap_max(l, i, len(l) - 1)

    # 注意，主要时间复杂度在这里 shift_heap() 的复杂度为 O(logn)，重复了 n 次
    while len(l) > 1:
        ret_list.append(l[0])
        l[0] = l.pop()
        shift_heap(l, 0, len(l) - 1)
        # shift_heap_max(l, 0, len(l) - 1)

    ret_list.append(l[0])
    return ret_list


def shift_heap(l, parent, end):
    '''
    :type l:        List[int]
    :type parent:   int
    :type end:      int

    节点下沉操作（小顶堆）
    '''
    while True:
        # 左子节点下标
        lchild = 2 * parent + 1
        # 右子节点下标
        rchild = 2 * parent + 2
        # 目标子节点下标
        child = lchild
        if child <= end:
            # 选择左右子节点中更小的一个进行比较
            child = rchild if rchild <= end and l[lchild] > l[rchild] else child
            if l[parent] > l[child]:
                l[parent], l[child] = l[child], l[parent]
                # 进行过交换，指向目标子节点继续下沉
                parent = child
            else:
                # 没有进行交换，表示符合小顶堆规则，直接返回
                break
        else:
            break


def shift_heap_max(l, parent, end):
    '''
    :type l:        List[int]
    :type parent:   int
    :type end:      int

    节点下沉操作（大顶堆）
    '''
    while True:
        lchild = 2 * parent + 1
        rchild = 2 * parent + 2
        child = lchild
        if child <= end:
            child = rchild if rchild <= end and l[lchild] < l[rchild] else child
            if l[parent] < l[child]:
                l[parent], l[child] = l[child], l[parent]
                parent = child
            else:
                break
        else:
            break


if __name__ == "__main__":
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(heap_sort(l))
