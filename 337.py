# coding: utf-8
''' 337. 打家劫舍 III

小偷又发现一个新的可行窃的地点。 这个地区只有一个入口，称为“根”。 除了根部之外，每栋房子有且只有一个父房子。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋形成了一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

在不触动警报的情况下，计算小偷一晚能盗取的最高金额。
'''


def makeTree(lt):
    """
    :type lt: List[int]
    :rtype: TreeNode
    """
    if lt == []:
        return None
    print(len(lt))
    parent = lt.pop(0)
    root = TreeNode(parent)
    current = root
    node_queue = []
    while lt != []:
        value = lt.pop(0)
        if value is not None:
            current.left = TreeNode(value)
            node_queue.append(current.left)
        if lt != []:
            value = lt.pop(0)
            if value is not None:
                current.right = TreeNode(value)
                node_queue.append(current.right)
            current = node_queue.pop(0)
    return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        d = self.dfs(root)
        return max(d)

    def dfs(self, node):
        """
        :type node: TreeNode
        :rtype: (int, int)

        其中返回值 res 中 res[0] 表示包含当前节点的最大值，res[1] 表示不包含当前节点的最大值
        """
        # 正确思路
        # if node is None:
        #     return (0, 0)
        # left_result = self.dfs(node.left)
        # right_result = self.dfs(node.right)
        # with_result = left_result[1] + right_result[1] + node.val
        # without_result = max(left_result) + max(right_result)
        # return (with_result, without_result)

        # 当时的错误思路：对于不包含当前节点的返回结果情况考虑不周，当时考虑的是既然不包含当前节点，那么对于左右子节点自然是至少包含一个才会导致不包含当前节点。
        # 实际上，这二者并无必然关系。因为我们的判断目标始终是以得到最大值为主，也有可能因为左右子节点的非当前节点结果已经很大了，所以会出现“断层”的现象：
        # 即两层节点都不选（两层以上节点都不选的情况不存在，因为多一个正数值就会变大这是自然的）。所以这不是一个 ~(res[1], res[1])) 的问题，而是求最大值组合的判断
        if node.left is None:
            left_result = (0, 0)
        else:
            left_result = self.dfs(node.left)
        if node.right is None:
            right_result = (0, 0)
        else:
            right_result = self.dfs(node.right)
        with_node_result = left_result[1] + node.val + right_result[1]
        max_without_node_result = max([
            (left_result[0] + right_result[0]),
            (left_result[1] + right_result[0]),
            (left_result[0] + right_result[1]),
            (left_result[1] + right_result[1])
        ])
        return (with_node_result, max_without_node_result)


class Solution2(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0, 0]
            robLeft = dfs(root.left)
            robRight = dfs(root.right)
            norobCur = robLeft[1] + robRight[1]
            robCur = max(robLeft[0] + robRight[0] + root.val, norobCur)
            return [norobCur, robCur]
        return dfs(root)[1]


if __name__ == '__main__':
    s = Solution()
    nums = [41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None, None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None, 31, 34, None,
            None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5, None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None, 22, None, 14, None, None, 21, 23]
    # nums = [1, 2, 10, 7, 9, 1, 2]
    root = makeTree(nums)
    print(s.rob(root))
