print("*** String Rotation ***")
string = input("Enter 2 strings : ").split()

temp1 = []
temp2 = []

for i in string[0]:
    temp1.append(i)
# print(temp1)
for i in string[1]:
    temp2.append(i)
# print(temp2)

# ก๊อปเก็บไว้เช็ค
checkTemp1 = temp1.copy()
checkTemp2 = temp2.copy()

# สลับ ตัวท้ายมาหน้า
# 1 2 3
temp1.insert(0, temp1[-1]) # 3 1 2 3
temp1.pop() # 3 1 2 ลบตัวท้าย

# 4 5 6
temp2.append(temp2[0]) # 4 5 6 4
temp2.pop(0) # 5 6 4

print("1 ", end = '')
for i in temp1:
    print(i, end='')
print(" ", end='')
for i in temp2:
    print(i, end='')
print("")

round = 1 # ทำขั้นทดลองมาเเล้ว 1
i = 2 # เข้าการปริ้นครั้งที่ 2
while temp1 != checkTemp1 or temp2 != checkTemp2:
    temp1.insert(0, temp1[-1]) # 2 3 1 2
    temp1.pop() # 2 3 1ลบตัวท้าย
    temp2.append(temp2[0]) # 5 6 4 5
    temp2.pop(0) # 6 4 5
    round = round+1
    if i<=5:
        print(i, end=' ')
        for j in temp1:
            print(j, end='')
        print(" ", end='')
        for j in temp2:
            print(j, end='')
        print("")
    i = i+1

# กรณีบรรทัดสุดท้ายคือบรรทัดที่ 6 
if  i == 7:
    print("6 ", end='')
    for i in temp1:
            print(i, end='')
    print(" ", end='')
    for i in temp2:
        print(i, end='')
    print("")
elif i > 7:
    print(" . . . . .")
    print(i-1, end=' ')
    for j in temp1:
        print(j, end='')
    print(" ", end='')
    for j in temp2:
        print(j, end='')
    print("")

print("Total of  " + str(round) + " rounds.")