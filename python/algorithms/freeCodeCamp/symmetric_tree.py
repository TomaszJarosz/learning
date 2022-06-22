def symetric_tree(root) -> bool:
    if root is None:
        return True

    return are_symetric(root.left, root.right)


def are_symetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symetric(root1.left, root2.right) and are_symetric(root1.right, root2.left)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
