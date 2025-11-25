class Queue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, item):
        self.queue.append(item)  
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.isEmpty():
            removed = self.queue.pop(0) 
            print(f"Dequeued element: {removed}")
            return removed
        else:
            print("Queue is empty! Cannot dequeue.")

    def peek(self):
        if not self.isEmpty():
            print(f"Front element: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty!")

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        print(f"Queue size: {len(self.queue)}")
        return len(self.queue)

    def printQueue(self):
        print(','.join(map(str, self.queue)))


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.size()
q.dequeue()
q.printQueue()

 