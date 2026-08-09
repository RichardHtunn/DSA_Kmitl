print(" *** Summation of each digit ***")
User_input = input("Enter a positive number : ").strip("")
total_sum = 0
for i in User_input:
    digit = int(i)
    total_sum = total_sum + digit
print(f"Summation of each digit =  {total_sum}")