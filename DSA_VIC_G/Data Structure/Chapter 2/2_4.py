User_input = input("Enter Your List : ").split(" ")

real_numbers = []
for i in User_input:
    convert = int(i)
    real_numbers.append(convert)

real_numbers.sort()

if len(real_numbers) <= 2:
    print("Array Input Length Must More Than 2")
else:
    final_result = []
    for i in range(len(real_numbers)):
        anchor = real_numbers[i]
        if anchor > 0:
            break

        if i > 0 and anchor == real_numbers[i - 1]:
            continue

        left = i + 1
        right = len(real_numbers) - 1

        while left < right:
            total = anchor + real_numbers[left] + real_numbers[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                final_result.append([anchor, real_numbers[left], real_numbers[right]])
                left += 1
                right -= 1
                while left < right and real_numbers[left] == real_numbers[left - 1]:
                    left += 1

    print(final_result)