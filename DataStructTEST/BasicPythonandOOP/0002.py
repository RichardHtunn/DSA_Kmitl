print(" *** Divisible number ***")
number = int(input("Enter a positive number : "))

store = []

if number == 0:
    print("0 is OUT of range !!!")
else:
    print("Output ==> ", end='')
    for i in range(1, number+1, 1):
        if number%i == 0:
            store.append(i)
            print(i, end=' ')
    print("")
    print("Total ==> ", end='')
    print(len(store))
