def mod_position(arr, s):
    emptyList = []
    for i in range(0, len(arr), 1):
        if (i+1) % s == 0:
            emptyList.append(arr[i])
    print(emptyList)

array, number = input("Enter Input : ").split(",")
number = int(number)

mod_position(array, number)