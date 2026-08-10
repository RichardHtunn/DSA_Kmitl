def gcd(number1, number2):
    if number1 == 0 and number2 == 0:
        print("Error! must be not all zero.")
        return 
    
    r = number1%number2
    if r == 0:
        return number2
    else:
        return gcd(number2, r)


inp = input("Enter Input : ").split()

temp = gcd ( int(inp[0]), int(inp[1]) )

if temp != None:
    print("The gcd of " + inp[0] + " and " + inp[1] + " is : ", end='')
    if temp < 0:
        print(abs(temp))
    else:
        print(temp)