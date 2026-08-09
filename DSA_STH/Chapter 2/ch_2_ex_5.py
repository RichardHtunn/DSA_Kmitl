class funString():
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        result = ""
        for char in self.string:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char) + 32)
            elif 97 <= ord(char) <= 122:
                result += chr(ord(char) - 32)
            else:
                result += char
        return result

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        result = ""
        for char in self.string:
            if char not in result:
                result += char
        return result

str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())