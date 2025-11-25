class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
        
node1 = Node(10)

node2 = Node(20)

node1.next = node2


print("First Node Data:", node1.data)
print("First Node Next:", "Exists" if node1.next else "None")

print("Second Node Data:", node2.data)
print("Second Node Next:", "Exists" if node2.next else "None")