class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
root = Node(1)

root.left = Node(2)
root.right = Node(3)


def inorder(node):
    if node:
        inorder(node.left)         # visit left subtree
        print(node.value, end=" ") # visit root
        inorder(node.right)        # visit right subtree

inorder(root)


def preorder(node):
    if node:
        print(node.value, end=" ") # visit root
        preorder(node.left)        # visit left subtree
        preorder(node.right)       # visit right subtree

preorder(root)


def postorder(node):
    if node:
        postorder(node.left)       # visit left subtree
        postorder(node.right)      # visit right subtree
        print(node.value, end=" ") # visit root

postorder(root)              

