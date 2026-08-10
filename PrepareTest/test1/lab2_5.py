import string

def bon(w):
    for i in range(len(w)):
        if i == len(w)-1:
            return "no same alphabet"
        else:
            if w[i] == w[i+1]:
                for j in range(len(string.ascii_lowercase)):
                    if w[i] == string.ascii_lowercase[j]:
                        return (j+1) * 4


secretCode = input("Enter secret code : ")
print(bon(secretCode))