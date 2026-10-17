def is_unimodal(arr, require_both_sides=False):
    """Check strict slopes; endpoint peaks are allowed unless requested otherwise."""
    if len(arr) < 3:
        return False

    index = 0

    while index + 1 < len(arr) and arr[index] < arr[index + 1]:
        index += 1

    peak_index = index

    if require_both_sides and not 0 < peak_index < len(arr) - 1:
        return False

    while index + 1 < len(arr) and arr[index] > arr[index + 1]:
        index += 1

    return index == len(arr) - 1


def find_peak_binary_search(arr, require_both_sides=False):
    # Validation is O(n); the binary search itself is O(log n).
    if len(arr) < 3:
        print("not enough")
        return -1

    if not is_unimodal(arr, require_both_sides):
        print("not a unimodal array")
        return -1

    left = 0
    right = len(arr) - 1

    while left < right:
        middle = (left + right) // 2

        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle

    return left


def find_peak_value(arr, require_both_sides=False):
    peak_index = find_peak_binary_search(arr, require_both_sides)
    return arr[peak_index] if peak_index != -1 else None


def main():
    try:
        numbers = list(map(int, input("Enter numbers : ").split()))
    except ValueError:
        print("Invalid input: enter integers separated by spaces")
        return

    # Change to True if the quiz requires a peak with both slopes.
    require_both_sides = False
    peak_index = find_peak_binary_search(numbers, require_both_sides)

    if peak_index != -1:
        print(f"Peak index: {peak_index}, Peak value: {numbers[peak_index]}")

    print()


if __name__ == "__main__":
    main()
