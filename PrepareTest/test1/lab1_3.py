print("*** Election ***")
print("Enter a number of voter(s) :", end=' ')
voter = float(input())

number = input().split()

while len(number) > voter:
    print("voter overflow")
    number.clear()
    number = input().split()
    
maxCount = 0
maxNumber = 0

for i in number:
    if int(i) > 20 or int(i) < 1:
        pass
    else:
        temp = number.count(i) # จำนวนของตัวเลขที่มากที่สุด
        if temp>maxCount:
            maxCount = temp
            maxNumber = i

if maxCount == 1 or maxCount == 0:
    print("*** No Candidate Wins ***")
else:
    print(maxNumber) 