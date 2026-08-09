def BubbleSort(items, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    return items

def SUMZero(items):
    final_list = []
    # let's loop the sorted list first
    n = len(items)
    # take the current one first, it is sorted
    for i in range(n-2):
        if i > 0 and items[i] == items[i-1]:
           continue 
        current = items[i]
        # my formula here, current = next one + last one
        j = i+1
        k = n-1
        while j < k: # loop thorough the whole list without overlapping
            total_sum = current + items[j] + items[k]
        # after summing, several conditions
        # this one is draining me
            if total_sum == 0:
                final_list.append([current, items[j], items[k]])
                j += 1
                k -= 1
                
                # FIX 4: Bypass identical numbers for j and k 
                # (This is what handles your [0, 0, 0, 0...] case safely)
                while j < k and items[j] == items[j - 1]:
                    j += 1
                while j < k and items[k] == items[k + 1]:
                    k -= 1
                    
            elif total_sum < 0:
                j += 1
            else:
                k -= 1
    return final_list

user_input = [int(x) for x in input("Enter Your List : ").split()]

# debugging line
# print(user_input)
n = len(user_input)
# condition to maintain at least len 3
if n >= 3:
    # debugging lines
    # print("sorting started")
    sorted_list = BubbleSort(user_input, n)
    # print("Sorting Done")
    # print(sorted_list)
else:
    print("Array Input Length Must More Than 2")

answer_list = SUMZero(sorted_list)
print(answer_list)
