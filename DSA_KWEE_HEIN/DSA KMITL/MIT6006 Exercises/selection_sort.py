# def selectionsortsmalltolarge(a):
    # n = len(a)
    # for i in range(n):
        # min_index = i
        # for j in range(i+1, n):
            # if a[j] < a[min_index]:
                # min_index = j
        # a[i], a[min_index] = a[min_index], a[i]
    # return a

# def selectionsortlargetosmall(a):
    # n = len(a)
    # for i in range(n):
        # max_index = i
        # for j in range(i+1,n):
            # if a[j] > a[max_index]:
                # max_index = j
            # a[i] ,a[max_index] = a[max_index], a[i]
    # return a
# # i, j and min
# array = input("Insert an input to sort: ")
# # logout
# numbers = []
# for a in array.split():
    # numbers.append(int(a))
# sorted_array = selectionsortsmalltolarge(numbers)
# print(sorted_array)
# sorted_array1 = selectionsortlargetosmall(numbers)
# print(sorted_array1)

# selection sort practice
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index], arr[i]
    return arr                


def selectionsortrevert(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            if arr[j] > arr[max_index]:
                max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
array = input("Insert an input to sort: ")
# logout
numbers = []
for a in array.split():
    numbers.append(int(a))
sorted_array = selectionsort(numbers)
print(sorted_array)

sorted_array = selectionsortrevert(numbers)
print(sorted_array)


