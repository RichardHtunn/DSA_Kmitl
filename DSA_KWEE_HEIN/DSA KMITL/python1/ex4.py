def odd_list(al):
    # put your code here
    result = []
    n = len(al)
    # debuggling line
    # print(n)
    if n > 1:
        for i in range(n):
            number = al[i]
            if number % 2 != 0:
                result.append(number)
                # print(result)
    else:
        print("The list must have at least one number")
    return result



print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
