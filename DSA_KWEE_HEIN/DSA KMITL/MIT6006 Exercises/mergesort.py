# # split array in half
# def mergesort(arr):
    # n = len(arr)
    # if n > 1:
        # # from start point to middle
        # left_arr = arr[:n//2]
        # # from middle to end point
        # right_arr = arr[n//2:]
    
        # mergesort(left_arr)
        # mergesort(right_arr)

        # # start sorting

        # i = 0 # index of left arr
        # j = 0 # index of right arr
        # k = 0 # index of final sorted arr

        # while i < len(left_arr) and j < len(right_arr):
            # # compare items in two arrays each
            # if left_arr[i] < right_arr[j]:
                # arr[k] = left_arr[i]
                # i += 1
            # else:
                # arr[k] = right_arr[j]
                # j += 1
            # k += 1

        # while i < len(left_arr):
            # arr[k] = left_arr[i]
            # i += 1
            # k += 1

        # while j < len(right_arr):
            # arr[k] = right_arr[j]
            # j += 1
            # k += 1
        
# # call merge sort on each halves recursively



# test_array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
# mergesort(test_array)
# print(test_array)

# mergesort in two functions
def mergesort(arr, a = 0, b = None):
    if b == None:
        b = len(arr)
    # check arr len
    if 1 < b - a:
        # make middle point
        c = (a + b) // 2
        mergesort(arr, a, c)
        mergesort(arr, c, b)
        L = arr[a:c]
        R = arr[c:b]
        merge(L, R, arr, len(L), len(R), a, b)
    return arr
# it is about merge function now
def merge(L, R, arr, i, j, a, b):
   # slice through every index
   if a < b:
       # when right arr is gone or leftarr len exists and left is greater than right
       if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
           arr[b-1] = L[i-1]
           i -= 1
       else:
           arr[b-1] = R[j-1]
           j -= 1
       merge(L, R, arr, i, j, a, b-1)



# test_arr  = [3, 5, 7, 2, 1, 8, 4, 9, 6 , 10, 12, 18, 11, 13]
# sorted_arr = mergesort(test_arr)
# print(sorted_arr)
user_input = input("Insert Number: ")

test_arr = []

for i in user_input.split():
    test_arr.append(int(i))

sorted_arr = mergesort(test_arr)
print(sorted_arr)