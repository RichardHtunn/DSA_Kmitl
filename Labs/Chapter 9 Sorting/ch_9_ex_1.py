def bubble_sort(arr):
    if len(arr) < 2:
        print(f"last step : {arr} move[None]")
        return

    for step in range(1, len(arr)):
        moved = None

        for i in range(len(arr) - step):
            if arr[i] > arr[i + 1]:
                moved = arr[i]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        if moved is None or step == len(arr) - 1:
            print(f"last step : {arr} move[{moved}]")
            break

        print(f"{step} step : {arr} move[{moved}]")


arr = list(map(int, input("Enter Input : ").split()))
bubble_sort(arr)