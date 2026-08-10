from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enQueue(self, new_data):
        self.items.append(new_data)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[0]

    def tail(self):
        if self.isEmpty():
            raise Exception("empty queue")
        return self.items[-1]

    def printWithOut(self):
        if len(self.items) == 0:
            print("[]", end=' ')
        else:
            # print('[', end='')
            for i in range(0, len(self.items), 1):
                # print("'", end='')
                print(self.items[i], end='')
                # print("'", end='')
                if i == len(self.items)-1:
                    pass
                else:
                    print(",", end=' ')


MyQueue = Queue()
YourQueue = Queue()

place = {'0':"Res.", '1':"ClassR.", '2':"SuperM.", '3':"Home"}
activity = {'0':"Eat", '1':"Game", '2':"Learn", '3':"Movie"}

inp = input("Enter Input : ").split(',')

for i in range(0, len(inp), 1):
    temp1 = inp[i][0:3]
    MyQueue.enQueue(temp1)
    temp2 = inp[i][4:]
    YourQueue.enQueue(temp2)

print("My   Queue =", end=' ')
MyQueue.printWithOut()
print("")
print("Your Queue =", end=' ')
YourQueue.printWithOut()
print("")

print("My   Activity:Location = ", end='')
for i in range(0, MyQueue.size(), 1):
    print(activity[MyQueue.items[i][0]], end=':')
    if i == MyQueue.size()-1:
        print(place[MyQueue.items[i][2]])
    else:
        print(place[MyQueue.items[i][2]], end=', ')

print("Your Activity:Location = ", end='')
for i in range(0, YourQueue.size(), 1):
    print(activity[YourQueue.items[i][0]], end=':')
    if i == YourQueue.size()-1:
        print(place[YourQueue.items[i][2]])
    else:
        print(place[YourQueue.items[i][2]], end=', ')

# check point
point = 0
for i in range(0, MyQueue.size(), 1):
    if MyQueue.items[i][0] == YourQueue.items[i][0] and MyQueue.items[i][2] != YourQueue.items[i][2]:
        point += 1
    elif MyQueue.items[i][0] != YourQueue.items[i][0] and MyQueue.items[i][2] == YourQueue.items[i][2]:
        point += 2
    elif MyQueue.items[i][0] == YourQueue.items[i][0] and MyQueue.items[i][2] == YourQueue.items[i][2]:
        point += 4
    elif MyQueue.items[i][0] != YourQueue.items[i][0] and MyQueue.items[i][2] != YourQueue.items[i][2]:
        point -= 5

if point >= 7:
    print("Yes! You're my love! : Score is "+str(point)+".")
elif point >= 0:
    print("Umm.. It's complicated relationship! : Score is "+str(point)+".")
else:
    print("No! We're just friends. : Score is "+str(point)+".")