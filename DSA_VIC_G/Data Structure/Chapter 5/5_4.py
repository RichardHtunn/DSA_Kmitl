class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class TextEditor:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None

    def insert(self, word):
        new_node = Node(word)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.cursor = new_node

        elif self.cursor == None:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.cursor = new_node

        else:
            new_node.next = self.cursor.next
            new_node.previous = self.cursor
            if self.cursor.next != None:
                self.cursor.next.previous = new_node
            else:
                self.tail = new_node
            self.cursor.next = new_node
            self.cursor = new_node

    def left(self):
        if self.cursor != None:
            self.cursor = self.cursor.previous

    def right(self):
        if self.cursor == None:
            if self.head != None:
                self.cursor = self.head

        elif self.cursor.next != None:
            self.cursor = self.cursor.next

    def backspace(self):
        if self.cursor != None:
            delete = self.cursor
            self.cursor = self.cursor.previous
            #to move the cursor back one step
            # bypass the tagget node by connecting next and previous
            if delete.previous != None:
                delete.previous.next = delete.next
            else:
                self.head = delete.next

            if delete.next != None:
                delete.next.previous = delete.previous
            else:
                self.tail = delete.previous

    def delete(self):
        if self.cursor == None:
            delete = self.head
        else:
            delete = self.cursor.next

        if delete != None:
            if delete.previous != None:
                delete.previous.next = delete.next
            else:
                self.head = delete.next

            if delete.next != None:
                delete.next.previous = delete.previous
            else:
                self.tail = delete.previous

    def __str__(self):
        output = []
        if self.cursor == None:
            output.append("|")

        current = self.head
        while current != None:
            output.append(current.data)
            if current == self.cursor:
                output.append("|")
            current = current.next
        return " ".join(output)

t = TextEditor()
User_input = input("Enter Input : ").split(",")
for i in User_input:
    i = i.strip()
    if i.startswith("I "):
        word = i[2:]
        t.insert(word)
    elif i.startswith("L"):
        t.left()
    elif i.startswith("R"):
        t.right()
    elif i.startswith("B"):
        t.backspace()
    elif i.startswith("D"):
        t.delete()
print(t)
         
