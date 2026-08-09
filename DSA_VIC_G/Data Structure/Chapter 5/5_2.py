class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublelyLinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None 

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        if self.isEmpty():
            return ""
        output = ""
        current = self.head
        while current != None:
            output += str(current.data)
            if current.next != None:
                output += "->"
            current = current.next
        return output

    def str_reverse(self):
        if self.isEmpty():
            return ""
        output = ""
        current = self.tail
        while current != None:
            output += str(current.data)
            if current.previous != None:
                output += "->"
            current = current.previous
        return output            

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def add_before(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert(self, index, data):
        index = int(index)
        s = self.size()
        if index < 0 or index > s:
            print("Data cannot be added")
            return
        print(f"index = {index} and data = {data}")

        if index == 0:
            self.add_before(data)
        elif index == s:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(index):
                current = current.next
            new_node.next = current
            new_node.previous = current.previous
            current.previous.next = new_node
            current.previous = new_node

    def remove(self, data):
        current = self.head
        index = 0
        while current != None:
            if str(current.data) == str(data):
                print(f"removed : {data} from index : {index}")

                if current.previous != None:
                    current.previous.next = current.next
                else: 
                    self.head = current.next

                if current.next != None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                return
            
            current = current.next
            index += 1
        print("Not Found!")

L = DoublelyLinkedList()
User_input = input("Enter Input : ").split(",")
for i in User_input:
    i = i.strip()
    if i.startswith("A "):
        data = i[2:]
        L.append(data)

    elif i.startswith("Ab "):
        data = i[3:]
        L.add_before(data)

    elif i.startswith("I "):
        parts = i[2:].split(":")
        index = parts[0]
        data = parts[1]
        L.insert(index, data)

    elif i.startswith("R "):
        data = i[2:]
        L.remove(data)

    print(f"linked list : {L}")
    print(f"reverse : {L.str_reverse()}")


