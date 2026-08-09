# bubble sort 
# we need temp variable here
arr = [9, 4, 2, 2,  3, 1, 8, 1 ]

# def upbubblesort(arr):
    # n = len(arr)
    # if n > 1:
     # # do bubblesorting here
        # for i in range(n-1):
            # for j in range(n-1-i):
                # if arr[j] > arr[j+1]:
                    # temp = arr[j]
                    # arr[j] = arr[j+1]
                    # arr[j+1] = temp
        # return arr
    # else:
        # print("The array must have at least two elements")
        # return 0

# def downbubblesort(arr):
    # n = len(arr)
    # if n > 1:
        # for i in range(n-1):
            # for j in range(n-1-i):
                # if arr[j] < arr[j+1]:
                    # temp = arr[j]
                    # arr[j] = arr[j+1]
                    # arr[j+1] = temp
        # return arr
    # else:
        # print("The array must have at least two numbers")
# sorted_arr = upbubblesort(arr)
# print(sorted_arr)


# sorted_arr = downbubblesort(arr)
# print(sorted_arr)

def Bubblesort(arr):
    n = len(arr)
    if n > 1:
        ## do the sorting
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr
    else:
        print("The length must be at least 2")

sorted_arr = Bubblesort(arr)
print(sorted_arr)
            