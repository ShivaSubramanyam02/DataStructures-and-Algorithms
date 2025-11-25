class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_of_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return sum_of_leaves(root.left) + sum_of_leaves(root.right)
