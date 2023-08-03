class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print(self):
        if self.head == None:
            print("Linked List is Empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def delete_value(self, value):
        if self.head == None:
            print("Linked List is Empty")
        else:
            if self.head.data == value:
                self.head = self.head.next
            else:
                current_node = previous_node = self.head
                while current_node.data != value:
                    previous_node = current_node
                    current_node = current_node.next
                previous_node.next = current_node.next

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        if not self.head:
            print("Linked List is Empty")
        else:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            print("Linked List is Empty")
        elif self.head.next == None:
            self.head = None
        else:
            current_node = previous_node = self.head
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = None

    def size(self):
        if not self.head:
            print("0, Empty linked list")
        else:
            count = 0
            current_node = self.head
            while current_node != None:
                count +=1
                current_node = current_node.next
            print("Linked List Size: ", count)

# ---------------------- Testing ----------------------
linkedlist = SinglyLinkedList()
print("Inserting 1, 2, 3, 4, 5:")
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)
linkedlist.insert(5)
linkedlist.print()
print("---------------------------------")
print("Delete 5:")
linkedlist.delete_value(5)
linkedlist.print()
print("---------------------------------")
print("Insert 0 at beginning:")
linkedlist.insert_at_beginning(0)
linkedlist.print()
print("---------------------------------")
print("Delete first element:")
linkedlist.delete_first()
linkedlist.print()
print("---------------------------------")
print("Delete last element:")
linkedlist.delete_last()
linkedlist.print()
print("---------------------------------")
print("Printing Linked List Size:")
linkedlist.size()
print("---------------------------------")