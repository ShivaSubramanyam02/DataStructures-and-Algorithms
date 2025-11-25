class stack():
    def __init__(self):
        self.stack = []
        
        
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed:{item}")
        
    
    def pop(self):
        if not self.isEmpty():
            popped = self.stack.pop()
            print(f"Popped Element :{popped}")
            return popped
        
        else:
            print("Stack is empty cannot pop")
            
    def peek(self):
        if not self.isEmpty():
            print(f"Top element: {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty")
            
            
    def isEmpty(self):
        return len(self.stack) == 0
    
    
    def size(self):
        print(f"stack size: {len(self.stack)}")
        
        return len(self.stack)
    
    
    def printStack(self):
        print(','.join(map(str, self.stack)))
    
s = stack()

s.push(10)
s.push(20)
s.push(30)
s.peek()
s.size()
s.pop()
s.printStack()
    







    



    
    
    

    
    
    






    