def ascending_sort(arr):
    values = [x for x in arr if x >= 0]

    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = key

    index = 0

    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i] = values[index]
            index += 1

    return arr


arr = list(map(int, input("Enter Input : ").split()))
print(*ascending_sort(arr))