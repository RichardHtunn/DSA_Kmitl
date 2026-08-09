class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Doubly_linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    # Forward String Representation
    def __str__(self):
        if self.isEmpty():
            return ""  # Return empty string so "linked list : " has nothing after it
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return "->".join(values)

    # Reverse String Representation
    def str_reverse(self):
        if self.isEmpty():
            return ""  # Return empty string so "reverse : " has nothing after it
        values = []
        current = self.tail
        while current is not None:
            values.append(str(current.data))
            current = current.previous
        return "->".join(values)

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
        self.length += 1

    def addBefore(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        self.length += 1

    def insert(self, index, data):
        idx = int(index)
        
        # 1. Guard against out-of-bounds indices FIRST
        if idx < 0 or idx > self.length:
            print("Data cannot be added")
            return

        # 2. Print insert success message only when index is valid
        print(f"index = {idx} and data = {data}")

        if idx == 0:
            self.addBefore(data)
            return

        if idx == self.length:
            self.append(data)
            return

        # Insertion in middle
        new_node = Node(data)
        current = self.head
        for _ in range(idx):
            current = current.next

        new_node.next = current
        new_node.previous = current.previous
        current.previous.next = new_node
        current.previous = new_node
        self.length += 1

    def remove(self, data):
        if self.isEmpty():
            print("Not Found!")
            return

        current = self.head
        index = 0
        while current and str(current.data) != str(data):
            current = current.next
            index += 1

        if not current:
            print("Not Found!")
            return

        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
        elif current == self.tail:
            self.tail = current.previous
            if self.tail:
                self.tail.next = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

        self.length -= 1
        print(f"removed : {data} from index : {index}")


# Command Parser
L = Doubly_linkedlist()
user_input = input("Enter Input : ").split(",")

for i in user_input:
    i = i.strip()
    
    if i.startswith("Ab"):
        data = i[2:].strip()
        L.addBefore(data)
    elif i.startswith("A"):
        data = i[1:].strip()
        L.append(data)
    elif i.startswith("I"):
        parts = i[1:].strip().split(":")
        index = parts[0]
        data = parts[1]
        L.insert(index, data)
    elif i.startswith("R"):
        data = i[1:].strip()
        L.remove(data)

    print(f"linked list : {L}")
    print(f"reverse : {L.str_reverse()}")
    
    
