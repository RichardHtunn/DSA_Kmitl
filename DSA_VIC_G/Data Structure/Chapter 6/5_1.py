def sum(n):
    if n <= 1:
        return "1", 1
    sequence, total = sum(n-1)
    return sequence + f" + {n}", total + n

print(" *** Natural sum ***")
User_input = int(input("Enter number : "))
sequence_str, final_total = sum(User_input)
print(f"{sequence_str} = {final_total}")
print("===== End of program =====")