class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###
        # constructor
        self.string = string 

    def __str__(self):

        ### Enter Your Code Here ###
        return self.string

    def size(self) :

        ### Enter Your Code Here ###
        # number of words in one word, not the length
        counter = 0
        for a in self.string:
            counter += 1
        
        return counter

    def changeSize(self):

        ### Enter Your Code Here ###
        # lower = upper + 32
        # upper = lower - 32
        result = []
        for a in self.string:
            # if a is uppercase
            if 'A' <= a <= 'Z':
                convert = ord(a) + 32
                result.append(chr(convert))
            # if a is lowercase:
            elif 'a' <= a <= 'z':
                convert = ord(a) - 32
                result.append(chr(convert))
            else:
                # if a is not a letter
                result.append(a)
        return "".join(result)

    def reverse(self):

        ### Enter Your Code Here ###
        # use slicing not builtin , write 
        result = []
        end = len(self.string) - 1
        # slicing starts from the end and gradually reduce until the first one
        for i in range(end, -1, -1):
            result.append(self.string[i])
        
        return "".join(result)

    def deleteSame(self):

       ### Enter Your Code Here ###
       # make a list first, loop, if same, skip it and not same, append
       result = []

       for char in self.string:
           if char not in result:
               result.append(char)
        
       return "".join(result)



str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())