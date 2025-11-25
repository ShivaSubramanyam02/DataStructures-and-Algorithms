class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    
def insert_at_head(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
    
    
def print_list(head):
    temp = head
    while temp:
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")
        
        
head = None
head = insert_at_head(head, 10)
head = insert_at_head(head, 20)

print_list(head)