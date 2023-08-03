class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        return bool(self.top == None)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        if self.is_empty():
            raise Exception("Displaying from an empty stack")
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.top.data

    def pop(self):
        if self.is_empty():
            raise Exception("Poping from an empty stack")
        self.top = self.top.next

    def size(self):
        if self.is_empty():
            raise Exception("Poping from an empty stack")
        count = 0
        current_node = self.top
        while current_node != None:
            count +=1
            current_node = current_node.next
        print("Linked List Size: ", count)


# ---------------------- Testing ----------------------
stack = Stack()
print("Push 1, 2, 3, 4:")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.display()
print("---------------------------------")
print("The Peek:")
print(stack.peek())
print("---------------------------------")
print("Pop an element:")
stack.pop()
stack.display()
print("---------------------------------")
print("The stack size:")
stack.size()
print("---------------------------------")