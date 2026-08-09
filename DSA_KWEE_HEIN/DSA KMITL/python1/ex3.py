# accept an integer
print(" *** Summation of each digit ***")

user_input = int(input("Enter a positive number : "))

if user_input > 0:
# count the digit and calculate it
    count = len(str(user_input))
    # debugging
    # print(count)
    if count <= 30:
        result = 0
        # use for loop and divide by ten, sum the remainder
        for i in range(count):
            # debugging line
            remainder = user_input % 10
            # print(remainder)
            result += remainder
            user_input = user_input // 10
            # debugging line
            # print(user_input)
        print(f"Summation of each digit =  {result}")

    

