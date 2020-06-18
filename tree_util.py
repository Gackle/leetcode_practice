class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.val}, [{self.left}, {self.right}])"


def initial_tree(l: list) -> TreeNode:
    parent_stack = []
    branch = 1  # 下一个添加的为左节点
    child = 1
    if len(l) < 1:
        return None
    root = TreeNode(l[0])
    pos = root
    while child < len(l):
        branch = (branch + 1) % 2
        if l[child] is not None:
            node = TreeNode(l[child])
            parent_stack.append(node)
        else:
            node = None
        if branch == 0:
            pos.left = node
        else:
            pos.right = node
            pos = parent_stack.pop(0)
        child += 1

    return root


def output_tree(root: TreeNode) -> list:
    # 遍历 TreeNode
    node_set = []
    total = 0

    def dfs(node: TreeNode, index: int):
        nonlocal total
        if node is None:
            return
        node_set.append((index, node.val))
        total = max(index, total)
        if node.left:
            dfs(node.left, 2*index+1)
        if node.right:
            dfs(node.right, 2*index+2)

    dfs(root, 0)
    result = ['null'] * (total + 1)
    for item in node_set:
        index = item[0]
        value = item[1]
        result[index] = value

    # 倒叙剪除多于的 null
    i = total
    while i >= 2:
        parent = (i - 1)//2 if i % 2 else i//2-1
        if parent >= 0 and result[i] == 'null' and result[parent] == 'null':
            del result[i]
        i -= 1

    return result


if __name__ == "__main__":
    l = [1, None, 3, 1, 2, 3]
    # l = [3, 9, 20, None, None, 15, 7]
    # l = [1, 401, None, 349, 88, 90]
    print(initial_tree(l))
    print(output_tree(initial_tree(l)))
