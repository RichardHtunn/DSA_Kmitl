def create_list(n):
    if n == 0:
        return []
    return [n] + create_list(n - 1)

def display(level):
    if level < 0:
        return
    a = list_A[level + 1] if level + 1 < len(list_A) else '|'
    b = list_B[level + 1] if level + 1 < len(list_B) else '|'
    c = list_C[level + 1] if level + 1 < len(list_C) else '|'
    print(f"{a}  {b}  {c}")
    display(level - 1)

def move(n, A, B, C, maxn):
    if n == 0:
        return
    move(n - 1, A, C, B, maxn)
    disk = A.pop()
    C.append(disk)
    print(f"move {disk} from  {A[0]} to {C[0]}")
    display(maxn)
    move(n - 1, B, A, C, maxn)

n = int(input("Enter Input : "))
list_A = ['A'] + create_list(n)
list_B = ['B']
list_C = ['C']

display(n)
move(n, list_A, list_B, list_C, n)