# from collections import deque


# class Queue:
#     def __init__(self):
#         self.items = []

#     def enQueue(self, i):
#         self.items.append(i)

#     def deQueue(self):
#         if not self.isEmpty():
#             return self.items.pop(0)
#         return None

#     def isEmpty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

#     def __str__(self):
#         return f"Queue(front -> {self.items} <- rear)"


# elements = [5, 7, 6, 3, 8, 4]
# print(f"Original list: {elements}\n")

# q = Queue()

# print("--- Enqueueing Elements ---")
# for num in elements:
#     q.enQueue(num)
#     print(f"Enqueued {num}: {q}")

# print("\n--- Dequeueing Elements ---")
# while not q.isEmpty():
#     removed_item = q.deQueue()
#     print(f"Dequeued {removed_item} | Remaining: {q}")

class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data)
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, data):
        self.next = next

p = Node('A', 'C')
p.setData('B')

print(p)



    
