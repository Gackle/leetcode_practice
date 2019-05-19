# coding: utf-8
''' 快速排序
'''


def quick_sort(l, reverse=False):
    '''
    :type l: List[int]
    :type reverse: bool
    :rtype: List[int]
    '''
    def little_quick_sort(entries: list) -> list:
        if len(entries) < 2:
            return entries
        elif len(entries) == 2:
            if entries[0] > entries[1]:
                entries.reverse()
            return entries
        left = []
        right = []
        mid = [entries[0]]
        for i in entries[1:]:
            if i > entries[0]:
                right.append(i)
            elif i < entries[0]:
                left.append(i)
            else:
                mid.append(i)
        return little_quick_sort(left) + mid + little_quick_sort(right)

    def great_quick_sort(entries: list) -> list:
        if len(entries) < 2:
            return entries
        elif len(entries) == 2:
            if entries[0] < entries[1]:
                entries.reverse()
            return entries
        left = []
        right = []
        mid = [entries[0]]
        for i in entries[1:]:
            if i < entries[0]:
                right.append(i)
            elif i > entries[0]:
                left.append(i)
            else:
                mid.append(i)
        return little_quick_sort(left) + mid + little_quick_sort(right)

    return great_quick_sort(l) if reverse else little_quick_sort(l)


if __name__ == "__main__":
    l = [93, 1, 23, 76, 32, 11, 35, 29, 7, 6674, 123, 1]
    print(quick_sort(l))
