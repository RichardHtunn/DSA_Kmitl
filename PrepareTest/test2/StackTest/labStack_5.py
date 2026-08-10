class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        # self.size = len(self.items)

    def push(self, i):
        self.items.append(i)
        # self.size += 1

    def pop(self):
        # self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        # return self.items = []
        return len(self.items) == 0

    def isFull(self):
        pass

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'stack of '+str(self.size())+' items : '
        for i in self.items:
            s += str(i)+' '
        return s


print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()

m,n = int(m),int(n)

Sgor = Stack()
Skoh = Stack()

if s != '0':
    for i in range(0, len(s), 1):
        if s[i] != ',':
            Sgor.push(int(s[i]))

if o == "arrive":
    if Sgor.size() == m:
        print("car", n, "cannot arrive : Soi Full")
    else:
        if n in Sgor.items:
            print("car", n, "already in soi")
        else:
            Sgor.push(n)
            print("car", n, "arrive! : Add Car", n)
elif o == "depart":
    if Sgor.isEmpty():
        print("car", n, "cannot depart : Soi Empty")
    else:
        if n not in Sgor.items:
            print("car", n, "cannot depart : Dont Have Car", n)
        else:
            while Sgor.peek() != n:
                temp = Sgor.pop()
                Skoh.push(temp)
            else:
                Sgor.pop()
                while not Skoh.isEmpty():
                    temp = Skoh.pop()
                    Sgor.push(temp)
            print("car", n, "depart ! : Car", n, "was remove")

print(Sgor.items)