def first_greater(arr, target, left, right):
    if left > right:
        return arr[left] if left < len(arr) else None

    mid = (left + right) // 2

    if arr[mid] > target:
        return first_greater(arr, target, left, mid - 1)

    return first_greater(arr, target, mid + 1, right)


inp = input("Enter Input : ").split("/")
arr = sorted(map(int, inp[0].split()))
targets = list(map(int, inp[1].split()))

for target in targets:
    result = first_greater(arr, target, 0, len(arr) - 1)
    print("No First Greater Value" if result is None else result)