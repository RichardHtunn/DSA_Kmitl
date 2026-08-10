def length(txt):
    if txt[1:] == "":
        print(txt[0], end='*')
        print("")
        return 1
    elif txt[2:] == "":
        print(txt[0], end='*')
        print(txt[1], end='~')
        print("")
        return 2
    else:
        print(txt[0], end='*')
        print(txt[1], end='~')
        return 2 + length(txt[2:])


inp = input("Enter Input :  ")
print(length(inp))