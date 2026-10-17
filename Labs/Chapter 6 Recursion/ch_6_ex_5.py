def staircase(n, i=1):
    if n == 0:
        return "Not Draw!"    
    abs_n = abs(n)    
    if n > 0:
        row = "_" * (abs_n - i) + "#" * i
    else:
        row = "_" * (i - 1) + "#" * (abs_n - i + 1)        
    if i == abs_n:
        return row
            
    return row + "\n" + staircase(n, i + 1)

print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
print("===== End of program =====")