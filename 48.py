# coding: utf-8
""" 48. 旋转图像

给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

提示：数组

思路：基本上坐标的转换可以马上想出来，关键是遍历的次数和顺序。当时想的过于简单，想通过分步骤或者对角线遍历得方法实现。
发现其实更加不现实。最后是通过洋葱层次遍历的方式实现（只遍历半个洋葱），而且还忘了不用 return，疯狂 N/A 😭
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or matrix == [[]]:
            return matrix
        n = len(matrix)
        half = n // 2
        
        for i in range(half):
            for j in range(i, n-i-1):
                # 其实换个思路，倒叙遍历 j 可以不用这么麻烦
                temp = matrix[i][j]
                temp, matrix[j][n-1-i] = matrix[j][n-1-i], temp
                temp, matrix[n-1-i][n-1-j] = matrix[n-1-i][n-1-j], temp
                temp, matrix[n-1-j][i] = matrix[n-1-j][i], temp
                temp, matrix[i][j] = matrix[i][j], temp
        # print(matrix)



if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # matrix = [[]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    s.rotate(matrix)