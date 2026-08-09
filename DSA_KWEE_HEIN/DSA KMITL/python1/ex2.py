# sum or multiplication
print("*** multiplication or sum ***")

user_input = input("Enter num1 num2 : ").split()

num1 = int(user_input[0])
num2 = int(user_input[1])

multi = num1 * num2

if multi <= 1000:
    print(f"The result is {multi}")
else:
    sum = num1 + num2
    print(f"The result is {sum}")
# print(num1)
# print(num2)