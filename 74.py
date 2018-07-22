# coding: utf-8
''' 74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

- 每行中的整数从左到右按升序排列。
- 每行的第一个整数大于前一行的最后一个整数。
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix == []:
            return False
        # 先查找行
        row_index = self.bin_search_row(0, len(matrix) - 1, matrix, target)
        if row_index == -1:
            return False
        # 后查找列
        return self.bin_search_column(0, len(matrix[row_index]) - 1, matrix[row_index], target)

    def bin_search_row(self, start, end, matrix, target) -> int:
        """
        :type start: int
        :type end: int
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        if start > end:
            return -1
        mid = (start + end) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        if matrix[mid][0] > target:
            return self.bin_search_row(start, mid - 1, matrix, target)
        elif matrix[mid][-1] < target:
            return self.bin_search_row(mid + 1, end, matrix, target)

    def bin_search_column(self, start, end, array, target) -> bool:
        """
        :type start: int
        :type end: int
        :type array: List[int]
        :type target: int
        :rtype: int
        """
        if start > end:
            return False
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        if array[mid] > target:
            return self.bin_search_column(start, mid - 1, array, target)
        elif array[mid] < target:
            return self.bin_search_column(mid + 1, end, array, target)


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    # matrix = [[1]]
    # target = 1
    print(s.searchMatrix(matrix, target))
