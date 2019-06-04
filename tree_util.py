class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def initialTree(li):
    '''
    :type li: List[int]
    '''
    if not li:
        return None
    root = buildTree(TreeNode(li[0]), 0, li)
    return root


def buildTree(parent: TreeNode, i: int, li: list) -> TreeNode:
    left = 2 * i + 1 if i > 0 and li[i - 1] is not None or i == 0 else i + 1
    right = 2 * i + 2 if i > 0 and li[i - 1] is not None or i == 0 else i + 2
    if left < len(li) and li[left] is not None:
        parent.left = buildTree(TreeNode(li[left]), left, li)
    else:
        parent.left = None
    if right < len(li) and li[right] is not None:
        parent.right = buildTree(TreeNode(li[right]), right, li)
    else:
        parent.right = None
    return parent


def initial_tree(l):
    d = {i: TreeNode(v) for i, v in enumerate(l) if v}
    for i, v in enumerate(l):
        if not v:
            continue
        d[i].left = d.get(2*i+1, None)
        d[i].right = d.get(2*i+2, None)
    return d[0] if d else None
