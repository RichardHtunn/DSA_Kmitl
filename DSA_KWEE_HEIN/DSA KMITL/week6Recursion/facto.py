# facto
def facR(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return n * facR(n-1)

print(" *** Factorial (Recursion) ***")
user_input =int(input("Enter Number : "))
answer = facR(user_input)
print(f"{user_input}! = {answer:,}")
print("===== End of program =====")