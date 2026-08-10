def shell(l, dIncrements):
    count = 0
    for inc in dIncrements:
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if j > inc:
                    count += 1
                if iEle<l[j-inc] and j > inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    
                    break
        count += 1

    return count

print(" *** Shell sort ***")
l = [int(i) for i in input("Enter some numbers : ").split()]
# print(l)
dIncrements = [3, 1]

x = shell(l, dIncrements)
print("")
print(l)

print("Data comparison =  " + str(x))