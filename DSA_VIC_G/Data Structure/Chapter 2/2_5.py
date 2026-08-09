class funString():
    def __init__(self,string = ""):
        self.my_string = string
    def __str__(self):
        return
    def size(self) :
        return len(str1)
    def changeSize(self):
        new_string = ""
        for i in self.my_string:
            if 65 <= ord(i) <= 90:
                total = ord(i) + 32
                new_string += chr(total)
            elif 97 <= ord(i) <= 122:
                total = ord(i) - 32
                new_string += chr(total)    
            else:
                new_string += i    
        return new_string   
    def reverse(self):
        new_string = ""
        for i in self.my_string:
            new_string = i + new_string
        return new_string
    def deleteSame(self):
        new_string = ""
        for i in self.my_string:
            if i in new_string:
                pass
            else:
                new_string += i
        return new_string

str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)
if str2 == "1" :    
    print(res.size())
elif str2 == "2":  
    print(res.changeSize())
elif str2 == "3" : 
    print(res.reverse())
elif str2 == "4" : 
    print(res.deleteSame())