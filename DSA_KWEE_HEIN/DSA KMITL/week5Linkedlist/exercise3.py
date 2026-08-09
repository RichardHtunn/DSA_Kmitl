class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
        self.data = int(data)
        self.next = next
    
    def __str__(self):
        ### Code Here ###
        return str(self.data)
        
def createList(l=[]):
    ### Code Here ###
    if not l:
        return None

    head = node(l[0])
    current = head
    for data in range(1, len(l)):
        current.next = node(l[data])
        current = current.next
    return head

def printList(H):
    ### Code Here ###
    current = H
    while current != None:
        print(current.data, end=' ')
        current = current.next
    print()

def mergeOrdersList(p, q):
    dummy = node(0)
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


#################### FIX comand ####################   
# input only a number save in L1,L2
user_input = input("Enter 2 Lists : ").split(" ")
L1 = user_input[0].split(",")
L2 = user_input[1].split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrdersList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)