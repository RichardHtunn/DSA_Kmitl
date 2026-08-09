# 6006 style
def merge_sort(arr, a=0, b= None):
    # divide arr into half
    if b == None:
        b = len(arr)
    # check the arr len is greater than one
    if 1 < b - a:
        c = (a + b) // 2
        merge_sort(arr, a, c)
        merge_sort(arr, c, b)
        # divide into two Left Right arrays
        L = arr[a:c]
        R = arr[c:b]
        merge(L, R, arr, len(L), len(R), a, b)
    return arr

# general merging function

def merge(L, R, arr, i, j, a, b):
    # looping around all arrs
    if a < b:
        # check about left side of arr
        # if right arr gone(all done) or left arr exists, item in L greater than in R
        if ( j <= 0) or ( i > 0 and L[i-1] > R[j-1]):
            # insert it to last index of final array
            arr[b-1] = L[i-1]
            i -= 1
        else:
            # insert the other side again
            arr[b-1] = R[j-1]
            j -= 1
        # merge again             # last one index of final arr in done so we use b-1 to repeat again
        merge(L, R, arr, i, j, a, b - 1)
    


# test_arr  = [3, 5, 7, 2, 1, 8, 4, 9]

test_arr  = [3, 5, 7, 2, 1, 8, 4, 9, 6 , 10, 12, 18, 11, 13]
sorted_arr = merge_sort(test_arr)
print(sorted_arr)


