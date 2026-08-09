print("*** multiplication or sum ***")
num1, num2 = input("Enter num1 num2 : ").split(" ")
num1, num2 = int(num1), int(num2)
if (num1 * num2) > 1000:
    result = num1 + num2
else:
    result = num1 * num2
print(f"The result is {result}")