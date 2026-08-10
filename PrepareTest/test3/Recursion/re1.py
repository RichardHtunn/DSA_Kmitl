def Fac(n):
    if n == 0:
        return 1
    if n==1:
        return 1
    else:
        return Fac(n-1) * n


inp = input("Enter Number : ")
inp = int(inp)
print(str(inp)+'! = ', Fac(inp), end='')