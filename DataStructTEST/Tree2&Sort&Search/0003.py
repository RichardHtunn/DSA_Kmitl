def insertion(l):
    count = 0
    for i in range(1, len(l), 1):
        iEle = l[i]
        for j in range(i, -1, -1):
            if j>=1:
                count += 1
            if iEle<l[j-1] and j>0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return count

print(" *** Insertion sort ***")
inp = [int(i) for i in input("Enter some numbers : ").split()]
x = insertion(inp)
print("")
print(inp)
print("Data comparison =  " + str(x))