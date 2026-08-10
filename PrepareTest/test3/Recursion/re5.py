def staircase(n, level=1):
    if n < 0:
        if n == -1:
            return "_"*(level-1) + "#"
        return "_"*(level-1) + "#"*abs(n) + "\n" + staircase(n+1, level+1)
    elif n > 0:
        if n == 1:
            return "#"*level
        return "_"*(n-1) + "#"*level + "\n" + staircase(n-1, level+1)
    elif n == 0:
        return "Not Draw!"

print(staircase(int(input("Enter Input : "))))