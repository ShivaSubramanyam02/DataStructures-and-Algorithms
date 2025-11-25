class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)
