class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    #convert Linked List into string
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        
        elements = []
        current = self.head
        while current != None:
            elements.append(str(current.value))
            current = current.next
        return " ".join(elements) #to print out with spaces in btw

    def addHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def search(self, data):
        current = self.head
        while current != None:
            if str(current.value) == str(data):
                return "Found"
            current = current.next
        return "Not Found"

    def index(self, data):
        count = 0
        current = self.head
        while current != None:
            if str(current.value) == str(data):
                return count
            count += 1
            current = current.next
        return -1

    def pop(self, position):
        position = int(position)
        if self.isEmpty() or position < 0 or position >= self.size():
            return "Out of Range"

        if position == 0:
            self.head = self.head.next
            return "Success"

        current = self.head
        for i in range (position - 1):
            current = current.next
        current.next = current.next.next
        return "Success"

L = LinkedList()
User_input = input("Enter Input : ").split(",")
for i in User_input:
    command = i[:2]
    data = i[3:]
    if command == "AP":
        L.append(data)
    if command == "AH":
        L.addHead(data)
    if command == "SE":
        print(f"{L.search(data)} {data} in {L}")
    if command == "ID":
        print(f"Index ({data}) = {L.index(data)} : {L}")
    if command == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    if command == "PO":
        before_list = str(L)
        result = L.pop(data)
        if result == "Success":
            print(f"{result} | {before_list} -> {L}")
        else:
            print(f"{result} | {L}")

print("Linked List :", L)




