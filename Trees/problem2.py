def sum_of_nodes(root):
    if root is None:
        return 0
    
    left_sum = sum_of_nodes(root.left)
    right_sum = sum_of_nodes(root.right)
    
    return root.value + left_sum + right_sum\
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(sum_of_nodes(root))  

