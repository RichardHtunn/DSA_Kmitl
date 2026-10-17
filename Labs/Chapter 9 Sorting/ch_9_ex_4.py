def insert_sorted(arr, value):
    arr.append(value)
    i = len(arr) - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = value


l = input("Enter Input : ").split()

if l[0] == "EX":
    Ans = "Insertion Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    l = list(map(int, l))
    original = []
    ordered = []

    for value in l:
        original.append(value)
        insert_sorted(ordered, value)
        n = len(ordered)

        if n % 2 == 1:
            median = float(ordered[n // 2])
        else:
            median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

        print(f"list = {original} : median = {median:.1f}")