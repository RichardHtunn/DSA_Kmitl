class node:
    def __init__(self, data, next=None):
        self.data = int(data)
        self.next = next
        
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if not l:
        return None

    head = node(l[0])
    current = head

    for i in range(1, len(l)):
        current.next = node(l[i])
        current = current.next
        
    return head

def printList(H):
    current = H
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()
def mergeOrderesList(p, q):
    dummy = node(0)
    tail = dummy

    while p is not None and q is not None:
        if p.data <= q.data:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    if p is not None:
        tail.next = p
    elif q is not None:
        tail.next = q

    return dummy.next

user_input = input("Enter 2 Lists : ")
list_strs = user_input.split(' ')

L1 = [int(x) for x in list_strs[0].split(',')]
L2 = [int(x) for x in list_strs[1].split(',')]

LL1 = createList(L1)
LL2 = createList(L2)

print('LL1 : ', end='')
printList(LL1)

print('LL2 : ', end='')
printList(LL2)

m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)