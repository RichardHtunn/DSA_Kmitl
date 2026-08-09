def move(n, A, B, C):
    if n == 1:
        print(n, 'from', A, 'to', C)
    else:
        move(n-1, A, B, C)
        print(n, 'from', A, 'to', C)
        move(n-1, B, C, A)
i = move(5, 1, 2, 4)
print(i)