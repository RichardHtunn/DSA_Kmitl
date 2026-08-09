print(" ***Function Odd List***")
User_input = input("Enter list numbers : ").split(" ")

real_numbers = []
for i in User_input:
    convert = int(i)
    real_numbers.append(convert)

odd_num = []
for j in real_numbers:
    if j % 2 != 0:
        odd_num.append(j)

print(f"Input list :  {real_numbers}")
print(f"Output list :  {odd_num}")

