class Queue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return f'Queue: {self.queue}'

    def is_empty(self):
        return len(self.queue) <= 0

    def inqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queue.pop()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[-1]

    def size(self):
        if self.is_empty():
            return "Queue is empty"
        return len(self.queue)

# ---------------------- Testing ----------------------
queue = Queue()
print("Push 1, 2, 3, 4:")
queue.inqueue(1)
queue.inqueue(2)
queue.inqueue(3)
queue.inqueue(4)
print(queue)
print("---------------------------------")
print("Pop an element:")
queue.dequeue()
print(queue)
print("---------------------------------")
print("The Peek:")
print(queue.peek())
print("---------------------------------")
print("Queue Size:")
print(queue.size())
print("---------------------------------")

