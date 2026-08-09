# def fac(n):
#     result = 1
#     for i in range(n, 0, -1):
#         result *= i
#     return result
# n = fac(5)
# print(n)

# def facR(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n* facR(n-1)
# m = facR(4)
# print(m)

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         lo, hi = 0, 1
#         for i in range(2, n+1):
#             new = hi + lo
#             lo = hi
#             hi = new
#         return new
# n = fib(10)
# print(n)

# def fibR(n):
#     if n <= 1:
#         return n
#     else:
#         return fibR(n-1) + fibR(n-2)
# n = fibR(8)
# print(n)

#Binary Search Recursive
# def search (low, high, x):
#     if high < low:
#         return -1
#     mid = (low+high) // 2
#     if x == a[mid]:
#         return(mid)
#     elif a[mid] < x:
#         return search (mid+1, high, x)
#     else:
#         return search (low, mid-1, x)
# a = [1, 3, 4, 5, 17, 18, 31, 33, 35]
# x = search(0, 8, 17.5)
# print(x)

# Backtracking
# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         x = fac (n-1)
#         return n * x
# i = fac(4)       
# print(i)

#Tower of Hanoi
# def move(n, A, B, C):
#     if n == 1:
#         print(n, 'from', A, 'to', C)
#     else:
#         move(n-1, A, B, C)
#         print(n, 'from', A, 'to', C)
#         move(n-1, B, C, A)
# i = move(5, 1, 2, 4)
# print(i)

# def PutQueenInRow (r, board, N):
#     global numsol
#     for c in range(N):
#         if (isSafe(board,r,c,N)):
#             board[r][c] = 1
#         if r == N-1:
#             print(board)
#             numsol += 1
#         else:
#             PutQueenInRow(r+1, board, N)
        
#         board[r][c] = 0