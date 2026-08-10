def mergesort(inp):
    global count
    
    if len(inp) > 1:
        midindex = (len(inp))//2

        leftlst = inp[:midindex]
        rightlst = inp[midindex:]

        mergesort(leftlst)
        mergesort(rightlst)

        indexleft = 0
        indexright = 0
        indexlst = 0
        
        while indexleft < len(leftlst) and indexright < len(rightlst):
            count += 1
            if leftlst[indexleft] <= rightlst[indexright]:
                inp[indexlst] = leftlst[indexleft]
                indexleft += 1

            else:
                inp[indexlst] = rightlst[indexright]
                indexright += 1
            indexlst += 1

        while indexleft < len(leftlst):
            inp[indexlst] = leftlst[indexleft]
            indexleft += 1
            indexlst += 1

        while indexright < len(rightlst):
            inp[indexlst] = rightlst[indexright]
            indexright += 1
            indexlst += 1

    return inp


print(" *** Merge sort ***")
inp = [int(i) for i in input("Enter some numbers : ").split()]

count = 0
x = mergesort(inp)

print()
print("Sorted ->", end=' ')

for i in inp:
    print(i, end=' ')

print("")

print("Data comparison = ", count)