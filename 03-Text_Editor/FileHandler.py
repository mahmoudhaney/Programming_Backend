def save_to_file(linkedlist):
    file_path = "03-Text_Editor/test.txt"
    try:
        # 1. Clearing file before inserting the data into it.
        with open(file_path, 'w') as file:
            file.write("")
        # 2. Inserting the data into it.
        current_node = linkedlist.head
        while current_node:
            with open(file_path, 'a') as file:
                file.write(current_node.data)
            current_node = current_node.next
        print("Successfully Saved")
    except FileNotFoundError:
        print("Something went wrong !!")

def read_file(linkedlist):
    file_path = "03-Text_Editor/test.txt"
    try:
        # 1. Get The data from the file
        with open(file_path, 'r') as file:
            data = file.readlines()
        # 2. Pushing the data into the linked list.
        for line in data:
            linkedlist.insert_back(line)
        if linkedlist.is_empty():
            print("!! File has no data to read !!")
        else:
            print("File Read Successfully")
    except FileNotFoundError:
        print("Something went wrong !!")