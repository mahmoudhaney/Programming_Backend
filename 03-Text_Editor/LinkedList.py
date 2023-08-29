import FileHandler

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return bool(self.count == 0)

    def display(self):
        if self.is_empty():
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def printing_with_numbering(self):
        if self.is_empty():
            print("Linked List is empty!")
        else:
            current_node = self.head
            node_number = 1
            print("------------------- Content -------------------")
            while current_node:
                print(node_number, ") " , current_node.data, end='', sep='')
                current_node = current_node.next
                node_number += 1
            print("## Number of Lines: ", self.count, " ##\n------------------- Content -------------------\n")

    def insert_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def insert_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def insert_in_betweeen(self, data, position):
        if position == 0:
            print("There's no line 0, Did you mean 1 !!!!")
        elif position == 1:
            self.insert_first(data)
        else:
            new_node = Node(data)
            current_node = self.head.next
            iterator = 2
            while current_node.next != None:
                if(iterator == position):
                    break
                current_node = current_node.next
                iterator += 1
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node
            self.count += 1

    def insert_before_tail(self, data):
        new_node = Node(data)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.count += 1

    def insert(self, data, position):
        if position == 0:
            print("There's no line 0, Did you mean 1 !!!!")
        else:
            if position == 1:
                self.insert_first(data)
            elif position > self.count:
                self.insert_back(data)
            elif position < self.count:
                self.insert_in_betweeen(data, position)
            elif position == self.count:
                selection = int(input("Enter 1 to replace the last line, enter 2 to insert a new line: "))
                if selection == 1:
                    self.replace_data(position, data)
                elif selection == 2:
                    self.insert_before_tail(data)
                else:
                    print("Invalid Choice !!")

    def replace_data(self, edited_data_position, new_data):
        if edited_data_position == 0:
            print("There's no line 0, Did you mean 1 !!!!")
        elif edited_data_position > self.count:
            print("Invalid Position !!!!")
        else:
            if edited_data_position == 1:
                self.head.data = str(self.head.data).replace(self.head.data, new_data)
            elif edited_data_position == self.count:
                self.tail.data = str(self.tail.data).replace(self.tail.data, new_data)
            else:
                current_node = self.head.next
                iterator = 2
                while current_node.next != None:
                    if(iterator == edited_data_position):
                        break
                    current_node = current_node.next
                    iterator += 1
                current_node.data = str(current_node.data).replace(current_node.data, new_data)

    def delete_first(self):
        if self.is_empty():
            print("Linked List is empty")
        elif self.count == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1

    def delete_last(self):
        if self.is_empty():
            print("Linked List is empty")
        elif self.count == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1

    def delete_node(self, position):
        current_node = self.head.next
        iterator = 2
        while current_node.next != None:
            if iterator == position:
                break
            current_node = current_node.next
            iterator += 1
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        current_node.next = current_node.prev = None
        self.count -= 1

    def delete_specific_node(self, position):
        if self.is_empty():
            print("Linked List is empty")
        else:
            if position == 0:
                print("There's no line 0, Did you mean 1 !!!!")
            elif position > self.count:
                print("Invalid Position !!!!")
            else:
                if position == 1:
                    self.delete_first()
                elif position == self.count:
                    self.delete_last()
                elif position < self.count:
                    self.delete_node(position)

    def num_of_node_data_char(self, position):
        if self.is_empty():
            print("Linked List is empty")
        else:
            if position == 0:
                print("There's no line 0, Did you mean 1 !!!!")
            elif position > self.count:
                print("Invalid Position !!!!")
            else:
                if position == 1:
                    print("Number of characters: ", len(self.head.data))
                elif position == self.count:
                    print("Number of characters: ", len(self.tail.data))
                else:
                    current_node = self.head.next
                    iterator = 2
                    while current_node.next != None:
                        if iterator == position:
                            break
                        current_node = current_node.next
                        iterator += 1
                    print("Number of characters: ", len(current_node.data) - 1)

    def save_all(self, linkedlist):
        if self.is_empty():
            print("!! Nothing to save, Linked list is empty !!")
        else:
            FileHandler.save_to_file(linkedlist)

    def read_file(self, linkedlist):
        FileHandler.read_file(linkedlist)
