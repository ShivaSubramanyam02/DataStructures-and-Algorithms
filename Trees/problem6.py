class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)

