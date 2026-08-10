class StackCalc:

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

    def run(self, message):
        number = ['0','1','2','3','4','5','6','7','8','9']
        stop = False
        
        for i in range(0, len(message), 1):
            if message[i] == '+':
                temp1 = self.items.pop()
                temp2 = self.items.pop()
                temp3 = int(temp1)+int(temp2)
                self.items.append(temp3)
            elif message[i] == '-':
                temp1 = self.items.pop()
                temp2 = self.items.pop()
                temp3 = int(temp1)-int(temp2)
                self.items.append(temp3)
            elif message[i] == '*':
                temp1 = self.items.pop()
                temp2 = self.items.pop()
                temp3 = int(temp1)*int(temp2)
                self.items.append(temp3)
            elif message[i] == '/':
                temp1 = self.items.pop()
                temp2 = self.items.pop()
                temp3 = int(temp1)/int(temp2)
                self.items.append(temp3)
            elif message[i] == "DUP":
                self.items.append(int(self.items[-1]))
            elif message[i] == 'POP':
                self.items.pop()
            else:
                for j in message[i]:
                    if j not in number:
                        print("Invalid instruction:", message[i])
                        return 'x'
                    else:
                        if j == message[i][-1]:
                            self.items.append(int(message[i]))

    def getValue(self):
        return int(self.items[-1])

print("* Stack Calculator *") 
arg = input("Enter arguments : ").split()
machine = StackCalc()
temp = machine.run(arg)
if temp != 'x':
    if machine.isEmpty():
        print('0')
    else:
        print(machine.getValue())