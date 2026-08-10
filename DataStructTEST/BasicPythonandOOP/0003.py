print(" *** String count ***")

countUpper = 0
countLower = 0

upper = []
lower = []

message = input("Enter message : ")

for i in range(0, len(message), 1):
    if message[i].isupper():
        countUpper += 1
        if message[i] not in upper:
            upper.append(message[i])
    elif message[i].islower():
        countLower += 1
        if message[i] not in lower:
            lower.append(message[i])
    else:
        pass


print("No. of Upper case characters :", countUpper)

print("Unique Upper case characters : ", end='')
upper.sort()
for i in upper:
    print(i, end='  ')
print("")

print("No. of Lower case Characters :", countLower)

print("Unique Lower case characters : ", end='')
lower.sort()
for i in lower:
    print(i, end='  ')