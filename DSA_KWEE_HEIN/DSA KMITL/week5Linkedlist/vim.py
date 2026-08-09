class Node:
    def __init__(self, data=""):
        self.data = data
        self.next = None
        self.prev = None

class TextEditor:
    def __init__(self):
        self.head = Node()
        self.cursor = self.head

    def insert(self, data):
        # inserting to the left with new node
        n = Node(data)
        # pointer allocate the new node with its neighbour two nodes
        # first connect n to neighbours
        n.next = self.cursor.next
        n.prev = self.cursor
        # do the remaining stuff with other nodes
        if self.cursor.next:
            self.cursor.next.prev = n
        self.cursor.next = n

        # put | infront of n node
        self.cursor = n

    def moveleft(self):
        if self.cursor != self.head:
            self.cursor = self.cursor.prev

    def moveright(self):
        if self.cursor.next is not None:
            self.cursor = self.cursor.next

    def deleteleft(self):
        if self.cursor != self.head:
            to_delete = self.cursor
            self.cursor = self.cursor.prev

            self.cursor.next = to_delete.next
            if to_delete.next:
                to_delete.next.prev = self.cursor

    def deleteright(self):
        if self.cursor.next is not None:
            to_delete = self.cursor.next
            self.cursor.next = to_delete.next
            if to_delete.next:
                to_delete.next.prev = self.cursor

    def display(self):
        result = []
        curr = self.head
        while curr is not None:
            if curr != self.head:
                result.append(curr.data)
            # Render | immediately after self.cursor
            if curr == self.cursor:
                result.append("|")
            curr = curr.next
        return " ".join(result)

L = TextEditor()
user_input = input("Enter Input : ").split(",")
for item in user_input:
    item = item.strip()
    if not item:
        continue
    if item[0] == "I":
        data = item[1:].strip()
        L.insert(data)   
    elif item[0] == "L":
        L.moveleft()
    elif item[0] == "R":
        L.moveright()
    elif item[0] == "B":
        L.deleteleft()
    elif item[0] == "D":
        L.deleteright()
    else:
        print("Incorrect Command !!! ")

answer = L.display()
print(answer)
    
    
        
