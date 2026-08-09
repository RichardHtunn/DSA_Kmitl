# divide in half, not in length, in value
# repeat the pattern
def BinarySearch(a, low, high, x):
    if high < low:
        return -1
    mid = (low+high) // 2
    if x == a[mid]:
        return mid
    elif a[mid] < x:
        return BinarySearch(a, mid +1, high, x)
    else:
        return BinarySearch(a, low,mid-1, x)

# 1. Parse space-separated input into a list of integers
user_input = [int(val) for val in input("Enter sorted numbers separated by space: ").split()]
n = len(user_input)

# 2. Pass boundary INDICES (0 and n-1), not element values
target = 17
answer = BinarySearch(user_input, 0, n - 1, target)

# 3. Display result
if answer != -1:
    print(f"Target {target} found at index: {answer}")
else:
    print(f"Target {target} not found in list.")
