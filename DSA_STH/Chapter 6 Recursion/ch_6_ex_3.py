def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

inp = input("Enter Input : ").strip()
idx = inp.find(' ')
a = int(inp[:idx])
b = int(inp[idx:].strip())

if a == 0 and b == 0:
    print("Error! must be not all zero.")
else:
    if a < b:
        a, b = b, a
    print(f"The gcd of {a} and {b} is : {gcd(abs(a), abs(b))}")