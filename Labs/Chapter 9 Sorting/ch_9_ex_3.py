def sort_digits(digits):
    result = digits[:]

    for i in range(1, len(result)):
        value = result[i]
        j = i - 1

        while j >= 0 and result[j] > value:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = value

    return result


digits = list(input("Enter Input : ").strip().lstrip("+-"))
ascending = sort_digits(digits)
duplicate = any(ascending[i] == ascending[i + 1]
                for i in range(len(ascending) - 1))

if ascending[0] == ascending[-1]:
    print("Repdrome")
elif digits == ascending:
    print("Plaindrome" if duplicate else "Metadrome")
elif digits == ascending[::-1]:
    print("Nialpdrome" if duplicate else "Katadrome")
else:
    print("Nondrome")