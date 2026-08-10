class MyInt:
    
    # constructor
    def __init__(self, number):
        self.number = number
        self.value = number

    # method
    def toRoman(self):
        roman = {1: 'I'
                , 4: 'IV'
                , 5: 'V'
                , 9: 'IX'
                , 10: 'X'
                , 40: 'XL'
                ,50: 'L'
                , 90: 'XC'
                , 100: 'C'
                , 400: 'CD'
                , 500: 'D'
                , 900: 'CM'
                , 1000: 'M'}

        divider = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for i in divider:
            if self.number != 0:
                temp = self.number//i
            
                if temp != 0:
                    for j in range(temp):
                        print(roman[i], end='')
            
            self.number = self.number%i
    
    def __add__(self, xx):
        return int((self.value + xx.value) * 1.5)


a = MyInt(500)

b = MyInt(40)

a.toRoman()
print("")
b.toRoman()

print(a+b)

# inp = input("Enter 2 number :").split()
# inp[0] = int(inp[0])
# inp[1] = int(inp[1])