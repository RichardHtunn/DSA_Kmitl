# class Queue:
#     def __init__(self, list = None):
#         if list == None:
#             self.items = []
#         else:
#             self.items = list
#     def enQueue(self, i):
#         self.items.append(i)
#     def deQueue(self):
#         return self.items.pop(0)
#     def isEmpty(self):
#         return self.items == []
#         #return len(self.items) == 0
# q = Queue()
# print(q.items)
# q.enQueue("A")
# print(q.items)
# q.enQueue("B")
# print(q.items)
# q.enQueue("C")
# print(q.items)
# print(q.deQueue())
# print(q.items)
# print(q.deQueue())
# print(q.items)
# print(q.isEmpty())

# L = [1,3,5,7,9]
# print(L)
# L.pop(0)
# print(L)
# L.insert(0, 2)
# print(L)

# from collections import deque 
# d = deque('def')
# print(d)
# d.append('g')
# d.append('h')
# print(d)
# pop1 = d.popleft()
# pop2 = d.popleft()
# print(d)
# print(pop1, pop2)
# print(len(d))

# from collections import deque
# class Queue:
#     def __init__(self, items = None):
#         self.items = deque()
#         if items is not None:
#             for item in items:
#                 self.enQueue(item)
#     def enQueue(self, i):
#         self.items.append(i)
#     def deQueue(self):
#         return self.items.popleft()
#     def IsEmpty(self):
#         return self.items == 0
#     def size(self):
#         return len(self.items)  
# L = [5,7,6,3,8,4]
# q = Queue(L)
# for i in L:
#     if q.size() > 0:
#         q.deQueue()
#         print(q.items)
#     else:
#         print(q.IsEmpty())

# class node:
#     def __init__(self, data, next = None):
#         self.data = data
#         if next is None:
#             self.next = None
#         else:
#             self.next = next
#     def __str__(self):
#         return str(self.data)
#     def getDat(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setDate(self, data):
#         self.data = data
#     def setNext(self, next):
#         self.next = next
# p = node('A', None)
# print(p)

# class list:
#     def __init__(self):
#         self.head = None
#     def __init__(self):
#         self.head = self.tail = None
#     def __init__(self, head = None):
#         if head == None:
#             self.head = self.tail = None
#             self.size = 0
#         else:
#             self.head = head
#             t = self.head
#             self.size = 1
#             while t.next != None:
#                 t = t.next
#                 self.size += 1
#             self.tail = t

class node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
class list:
    def __init__(self):
        self.head = None
    def append(self, data):
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
i = list()
i.append('A')
print(i)