def quick_sort(arr, strategy):
    arr = arr[:]

    def sort(left, right):
        if left >= right:
            return 0

        if strategy == "First":
            pivot_index = left
        elif strategy == "Last":
            pivot_index = right
        else:
            pivot_index = (left + right) // 2

        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
        pivot = arr[left]
        position = left
        comparisons = 0

        for i in range(left + 1, right + 1):
            comparisons += 1

            if arr[i] < pivot:
                position += 1
                arr[position], arr[i] = arr[i], arr[position]

        arr[left], arr[position] = arr[position], arr[left]

        comparisons += sort(left, position - 1)
        comparisons += sort(position + 1, right)

        return comparisons

    return sort(0, len(arr) - 1)


print(" *** Quick sort ***")
numbers = list(map(int, input("Enter a sequence of integers : ").split()))

print("\nNumber of comparisons for each pivot strategy:")

for strategy in ("First", "Last", "Middle"):
    count = quick_sort(numbers, strategy)
    print(f"{strategy} Pivot: {count} comparisons")

print("===== End of program =====")