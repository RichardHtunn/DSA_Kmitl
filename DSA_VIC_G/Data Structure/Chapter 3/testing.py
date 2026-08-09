# class Stack:
#     """ class Stack
#         create empty stack"""
#     def __init__(self):
#         self.items = []
# s = Stack()
# print(s.items)

# class Stack:
#     """ class Stack
#         default : empty stack /
#         Stack([list])"""
#     def __init__(self, list = None):
#         if list == None:
#             self.items = []
#         else:
#             self.items = list
# s = Stack()
# print(s.items)
# s1 = Stack(["A", "B", "C"])
# print(s1.items)

# i = 5
# def f(arg = i + 2):
#     print(arg)
#     arg = 0
#     print(arg)
#     print("-----")
# i = 6
# f()
# f(3)
# f()

# def f(L = []):
#     print(L)
#     L.append(1)
# f()
# f()
# f([2])
# f()

# def f(x, L = None):
#     if L is None:
#         L = []
#     L.append(x)
#     return(L)
# print(f(1))
# print(f(2))
# print(f(0, [5, 6]))
# print(f(3))

#push pop peek 
class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def __str__(self):
        s = 'stack of' + str(self.size()) + 'items :'
        for ele in self.items:
            s += str(ele) + ''
        return s
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-2]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
s = Stack()
print(s.items)
s.push("A")
s.push('B')
s.push('C')
print(s.items)
print(s.pop())
print(s.items)
print(s.peek())
print(s.items)
print(s.isEmpty())
print(s.size())
s1 = Stack([1,2,3,4])
print(s1.items)
print(s1)