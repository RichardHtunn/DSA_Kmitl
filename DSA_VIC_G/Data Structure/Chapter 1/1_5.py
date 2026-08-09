User_input = input("Enter All Bid : ").split(" ")

real_numbers = []
for i in User_input:
    convert = int(i)
    real_numbers.append(convert)

length = len(real_numbers)
for j in range(length):
    for i in range(length - 1):
        if real_numbers[i] > real_numbers[i + 1]:
            num = real_numbers[i]
            real_numbers[i] = real_numbers[i + 1]
            real_numbers[i + 1] = num

if length < 5:
    print("not enough bidder")
elif real_numbers[-1] == real_numbers[-2]:
    print("error : have more than one highest bid")
else:
    print(f"winner bid is {real_numbers[-1]} need to pay {real_numbers[-2]}")