def odd_list(al):
    result = []
    for x in al:
        if x % 2 != 0:
            result.append(x)
    return result

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)