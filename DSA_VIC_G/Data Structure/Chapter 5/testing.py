# class node:
#     def __init__(self, data, next=None):
#         self.data = data
#         if next is None:
#             self.next = None
#         else:
#             self.next = next
#     def __str__(self):
#         return str(self.data)
#     def getData(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setData(self, data):
#         self.data = data
#     def setNext(self, next):
#         self.next = next
# p = node('A', None)
# print(p)

# class list:
#     def __init__(self):
#         ''' unordered singly linked list with head'''
#         self.head = None
#     def __init__(self):
#         ''' unordered singly linked list with head & tail'''
#         self.head = self.tail = None
#     def __init__(self, head=None):
#         ''' unordered singly linked list can set default list with head, tail & size'''
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

class list:
    def __init__(self):
        ''' unordered singly linked list with head'''
        self.head = None
    def append(self, data):
        ''' add at the end of list '''
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
class node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
I = list()
I.append('A')
p = node('A', None)
print(p.data)
