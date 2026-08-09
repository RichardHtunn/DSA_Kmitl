print(" *** Summation of each digit ***")
user_input = input("Enter a positive number : ").strip()

digits = [char for char in user_input if char.isdigit()]

if not digits:
    print("Error")

total_sum = sum(int(d) for d in digits)

        
print(f"Summation of each digit =  {total_sum}")

