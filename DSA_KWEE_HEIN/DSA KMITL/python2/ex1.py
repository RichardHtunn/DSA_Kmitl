class Calculator :

    ### Enter Your Code Here ###

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        ###Enter Your Code For Add Number###
        sum = self.value + other.value
        return sum
        

    def __sub__(self, other):
         ###Enter Your Code For Sub Number### 
         substract = self.value- other.value
         return substract

    def __mul__(self, other):
        ###Enter Your Code For Mul Number###
            multi = self.value * other.value
            return multi

    def __truediv__(self, other):
         
        if other.value == 0:
             return "Error"
        else:
             division = self.value / other.value
             return division

        ###Enter Your Code For Div Number###

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")