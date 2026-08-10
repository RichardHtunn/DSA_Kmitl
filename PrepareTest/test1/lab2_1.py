class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return int(self.num1) + int(self.num2)

    def sub(self):
        return int(self.num1) - int(self.num2)

    def mul(self):
        return int(self.num1) * int(self.num2)

    def truediv(self):
        return float(self.num1) / float(self.num2)


x, y = input("Enter num1 num2 : ").split(",")

p = Calculator(x, y)

print(p.add())
print(p.sub())
print(p.mul())
print(p.truediv())