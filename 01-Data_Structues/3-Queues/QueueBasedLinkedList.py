class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None

    def is_empty(self):
        return (self.front == None and self.rear == None)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current_node = self.front
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def inqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.front.data)

    def size(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            count = 0
            current_node = self.front
            while current_node:
                count += 1
                current_node = current_node.next
            print("Queue Size: ", count)

# ---------------------- Testing ----------------------
queue = Queue()
print("Push 1, 2, 3, 4:")
queue.inqueue(1)
queue.inqueue(2)
queue.inqueue(3)
queue.inqueue(4)
queue.display()
print("---------------------------------")
print("Pop an element:")
queue.dequeue()
queue.display()
print("---------------------------------")
print("The Peek:")
queue.peek()
print("---------------------------------")
print("The Queue Size")
queue.size()
print("---------------------------------")