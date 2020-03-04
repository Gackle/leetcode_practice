# coding: utf-8
""" 1104. 二叉树寻路

在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

 

示例 1：
输入：label = 14
输出：[1,3,4,14]

示例 2：
输入：label = 26
输出：[1,2,6,10,26]
"""


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        result = []
        # 判断lable的行
        n = 1
        while label >= 2**n:
            n += 1
        cur = label
        result.append(cur)
        index = 2**n-1-label if not n % 2 else label-2**(n-1)
        n -= 1
        while n > 0:
            index = index // 2
            cur = 2**(n-1)+index if n % 2 else 2**n-1-index
            result.append(cur)
            n -= 1
        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    label = 16
    print(s.pathInZigZagTree(label))
