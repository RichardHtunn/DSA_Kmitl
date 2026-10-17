# class Stack:
    
#     def __init__(self, initial_list=None):
#         if initial_list is None:
#             self.items = []
#         else:
#             self.items = initial_list
        
#     def __str__(self):
#         s = "Stack of " + str(len(self.items)) + " items: "

#         for element in self.items:
#             s += str(element) + ' '
#         return s
    
#     def push(self, i):
#         self.items.append(i)

#     def pop(self):
#         return self.items.pop()
    
#     def peek(self):
#         return self.items[-1]

#     def isEmpty(self):
#         return self.items == []
    
#     def size(self):
#         return len(self.items)


# s = Stack()

# s.push("A")
# s.push("B")
# s.push("C")
# print(s)


# print(s.pop())
# print(s)

# print(s.peek())
# print(s)

# print(s.isEmpty())

# print(s.size())

# s1 = Stack([1,2,3])
# print(s1.items)


class Sphere:
    def __init__ (self, radius):
        self.radius = radius
    
    def volume(self):
        return (4/3.0) * 3.14159 * (self.radius ** 3)