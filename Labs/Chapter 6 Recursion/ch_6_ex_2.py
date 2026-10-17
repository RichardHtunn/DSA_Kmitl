print(" *** Length of string (Recursion) ***")
inp = input("Enter Input : ")

def length(txt):
    if txt == "":
        return 0
    if txt[1:] == "":
        print(txt[0] + "*", end="")
        return 1
    print(txt[0] + "*" + txt[1] + "~", end="")
    return 2 + length(txt[2:])

print(f"\nlength of '{inp}' is {length(inp)}")