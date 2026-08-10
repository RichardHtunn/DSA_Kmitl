def gcd(number1, number2):
    number1 = abs(number1)
    number2 = abs(number2)

    if number1 == 0:
        if number2 == 0:
            return 0
        else:
            return number2
    elif number2 == 0:
        return number1
    
    temp = abs(number1-number2)
    if temp == 0:
        return number1
    else:
        if number1 > number2:
            return gcd(temp, number2)
        else:
            return gcd(temp, number1)


number1, number2 = input("Enter Input : ").split(" ")
number1 = int(number1)
number2 = int(number2)

if number1 == 0 and number2 <=0 or number2 == 0 and number1 <=0:
    x = number1
    y = number2
else:
    x = abs(number1)
    y = abs(number2)
    

if x > y:
    print("The gcd of "+str(number1)+" and "+str(number2)+" is :",gcd(number1,number2))
elif x < y:
    print("The gcd of "+str(number2)+" and "+str(number1)+" is :",gcd(number1,number2), end='')
elif x == y:
    if number1 == 0 and number2 == 0:
        print("Error! must be not all zero.")
    else:
        print("The gcd of "+str(number1)+" and "+str(number2)+" is :",gcd(number1,number2))