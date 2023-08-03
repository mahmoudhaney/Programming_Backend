class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return bool(self.head == None)

    def display(self):
        if self.is_empty():
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def display_reverse(self):
        if self.is_empty():
            print("Linked List is empty")
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            while last_node:
                print(last_node.data)
                last_node = last_node.prev

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            new_node.prev = last_node
            last_node.next = new_node

    def delete_first(self):
        if self.is_empty():
            print("Linked List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_back(self):
        if self.is_empty():
            print("Linked List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.prev.next = None
# ---------------------- Testing ----------------------
linkedlist = DoublyLinkedList()
print("Inserting 2, 3 from back:")
linkedlist.insert_back(2)
linkedlist.insert_back(3)
linkedlist.display()
print("---------------------------------")
print("Inserting 1, 0 from first:")
linkedlist.insert_first(1)
linkedlist.insert_first(0)
linkedlist.display()
print("---------------------------------")
print("Display in reverse:")
linkedlist.display_reverse()
print("---------------------------------")
print("Delete the first element:")
linkedlist.delete_first()
linkedlist.display()
print("---------------------------------")
print("Delete the last element:")
linkedlist.delete_back()
linkedlist.display()
print("---------------------------------")