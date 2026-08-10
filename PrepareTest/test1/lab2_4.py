eList = []

list = input("Enter Your List : ").split()
for i in range(len(list)):
    list[i] = int(list[i])

if len(list) <= 2:
    print("Array Input Length Must More Than 2")
else:
    for i in range(0, len(list), 1):
        for j in range(i+1, len(list), 1):
            for k in range(j+1, len(list), 1):
                if list[i]+list[j]+list[k] == 0:
                    if [list[i], list[j], list[k]] in eList:
                        pass
                    else:
                        eList.append([list[i], list[j], list[k]])
    print(eList)