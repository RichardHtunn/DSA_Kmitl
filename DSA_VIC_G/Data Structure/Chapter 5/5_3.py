class Node():
    def __init__(self, data, next = None):
        self.data = int(data)
        self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l:
        return None

    head = Node(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = Node(l[i])
        current = current.next
    return head

def printList(H):
    current = H
    while current != None:
        print(current.data, end=' ')
        current = current.next
    print()

def mergeOrdersList(p, q):
    dummy = Node(0)
    current = dummy
    while p != None and q != None:
        if p.data <= q.data:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next
        current = current.next

    if p == None:
        current.next = q

    if q == None:
        current.next = p
    return dummy.next

User_input = input("Enter 2 Lists : ").split(" ")
list1 = User_input[0].split(",")
list2 = User_input[1].split(",")
LL1 = createList(list1)
LL2 = createList(list2)
print("LL1 : ", end='')
printList(LL1)
print("LL2 : ", end='')
printList(LL2)
m = mergeOrdersList(LL1, LL2)
print("Merge Result : ", end='')
printList(m)