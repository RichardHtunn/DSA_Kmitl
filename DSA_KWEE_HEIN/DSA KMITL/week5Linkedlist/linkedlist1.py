# singly linked list
# singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        s = ""
        while cur is not None:
            s += cur.value + " "
            cur = cur.next
        return s.strip()

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.length += 1

    def addHead(self, item):
        p = Node(item)
        p.next = self.head
        self.head = p
        self.length += 1

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def index(self, item):
        current = self.head
        idx = 0
        while current is not None:
            if current.value == item:
                return idx
            current = current.next
            idx += 1
        return -1

    def size(self):
        return self.length

    def pop(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.length:
            return "Out of Range"

        if pos == 0:
            self.head = self.head.next
            return "Success"
        else:
            prev = self.head
            for _ in range(pos - 1):
                prev = prev.next
            prev.next = prev.next.next

        self.length -= 1
        return "Success"

L = LinkedList()
inp = input("Enter Input : ").split(",")

for i in inp:
    cmd = i[:2]
    arg = i[3:]

    if cmd == "AP":
        L.append(arg)

    elif cmd == "AH":
        L.addHead(arg)

    elif cmd == "SE":
        if L.isEmpty():
            print(f"Not Found {arg} in Empty")
        elif L.search(arg):
            print(f"Found {arg} in {L} ")
        else:
            print(f"Not Found {arg} in {L} ")

    elif cmd == "SI":
        print(f"Linked List size = {L.size()} : {L} ")

    elif cmd == "ID":
        print(f"Index ({arg}) = {L.index(arg)} : {L} ")

    elif i[:2] == 'PO':
        before = f"{L}"
        k = L.pop(int(i[3:]))
        if k == "Success":
            print(f"{k} | {before} -> {L}")
        else:
            print(f"{k} | {L} ")

print("Linked List :", L )