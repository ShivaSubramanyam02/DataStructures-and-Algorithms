class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_internal_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)
