def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        low, high = 0 , 1
        for i in range(2, n+1):
            low, high = high , low + high
        return high

user_input =int(input("Enter a number : "))
answer = fib(user_input)
print(answer)