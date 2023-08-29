import LinkedList
doubly_linked_list = LinkedList.DoublyLinkedList()

def pick_choice():
    while True:
        try:
            Menu()
            choice = int(input("Choose a process: "))
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                handle_choice(choice)
            elif choice == 8:
                print("<3 <3 Thank You <3 <3")
                break
            else:
                print("Oops!! - Unknown Choice")
        except ValueError:
            print("!! Invalid Choice !!")

def Menu():
    print("<-<-<-<-<-<-<-<-<-< TEXT EDITOR >->->->->->->->->->")
    print(  "1. Insert New Line N\n" + 
            "2. Delete A Line N\n" +
            "3. Replace Text in Line N\n" + 
            "4. Print All\n" + 
            "5. How many characters in Line N\n" + 
            "6. Save into the file\n" + 
            "7. Read a file\n" + 
            "8. Exit")
    print("<-<-<-<-<-<-<-<-<-<-<-<-<- ->->->->->->->->->->->->->")

def handle_choice(choice):
    match choice:
        case 1:
            line_position = int(input("Enter the Line Position To Insert: "))
            if line_position == 0:
                print("There's no line 0, Did you mean 1 !!!!")
            else:
                data = input("Enter the text: ")
                data += "\n"
                doubly_linked_list.insert(data, line_position)
        case 2:
            line_position = int(input("Enter the Line Position To Delete: "))
            doubly_linked_list.delete_specific_node(line_position)
        case 3:
            if doubly_linked_list.is_empty():
                print("You can't replace any line, The linked List is Empty")
            else:
                line_position = int(input("Enter the Line Position To Replace: "))
                new_data = input("Enter the new text: ")
                new_data += "\n"
                doubly_linked_list.replace_data(line_position, new_data)
        case 4:
            doubly_linked_list.printing_with_numbering()
        case 5:
            if doubly_linked_list.is_empty():
                print("You can't replace any line, The linked List is Empty")
            else:
                line_position = int(input("Enter the Line Position To Count: "))
                doubly_linked_list.num_of_node_data_char(line_position)
        case 6:
            doubly_linked_list.save_all(doubly_linked_list)
        case 7:
            doubly_linked_list.read_file(doubly_linked_list)
        case 8:
            return
        case _:
            print("Unknown Choice")

def main():
    pick_choice()

if __name__ == "__main__":
    main()