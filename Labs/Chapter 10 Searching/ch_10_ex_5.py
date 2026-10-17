def sort(inp):
    for i in range(1, len(inp)):
        value = inp[i]
        j = i - 1

        while j >= 0 and inp[j] > value:
            inp[j + 1] = inp[j]
            j -= 1

        inp[j + 1] = value

    return inp


def binary_search(inp, q):
    left = 0
    right = len(inp) - 1
    count = 0

    print(f"Searching for {q}")
    print("round|\tleft|\tright|\tmiddle|")

    while left <= right:
        count += 1
        mid = (left + right) // 2
        print(f"{count:>5}|\t{left:>4}|\t{right:>5}|\t{mid:>6}|")

        if inp[mid] == q:
            return [mid, count, left, right]

        if inp[mid] < q:
            left = mid + 1
        else:
            right = mid - 1

    return [-1, count, left, right]


inp, q = input("Enter list of numbers: ").split("/")
inp = [int(i) for i in inp.split()]
q = [int(i) for i in q.split()]
inp = sort(inp)

print("Sorted list: ", end="")
print(*inp)

for value in q:
    res = binary_search(inp, value)

    if res[0] == -1:
        print(f"Not found {value} in the list")
    else:
        print(f"Found {value} at index {res[0]}")
        print(f"[round/left/right] : {res[1]} {res[2]} {res[3]}")

    print()