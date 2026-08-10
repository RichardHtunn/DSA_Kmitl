def max(inp):
    if len(inp) == 1:
        return inp[0]
    else:
        maxValue = max(inp[1:])
        if  maxValue > inp[0]:
            return maxValue
        else:
            return inp[0]

inp = input("Enter Input : ").split()

for i in range(len(inp)):
    inp[i] = int(inp[i])

print("Max : ", end='')
print(max(inp))