class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __str__(self) -> str:
        return f'Stack: {self.stack}'

    def is_empty(self):
        return len(self.stack) <= 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.stack.pop() # OR: self.stack.remove(self.stack[-1])

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack[-1]


# ---------------------- Testing ----------------------
stack = Stack()
print("Push 1, 2, 3, 4:")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print("---------------------------------")
print("Pop an element:")
stack.pop()
print(stack)
print("---------------------------------")
print("The Peek:")
print(stack.peek())
print("---------------------------------")

