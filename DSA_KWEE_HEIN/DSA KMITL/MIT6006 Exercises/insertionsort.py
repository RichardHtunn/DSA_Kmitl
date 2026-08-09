# insertion sort
arr = [0, 5, 8, 9, 7, 11, 1, 13, 45]
def insertionsort(arr):
    n = len(arr)
    if n > 1:
        ## do the process
        ## here we have to keep the left side as unsorted
        for i in range(1,n):
            current_index = i
            current_value = arr[i]
            for j in range(i-1, -1, -1):
                if arr[j] > current_value:
                    arr[j+1] = arr[j]
                    current_index = j
                else:
                    break
            arr[current_index] = current_value
    else:
        print("The length must be at least two")

    return arr    

sorted_arr = insertionsort(arr)
print(sorted_arr)