print("*** New Range ***")
User_input = input("Enter Input : ").split(" ")

real_numbers = []
for i in User_input:
    convert = float(i)
    real_numbers.append(convert)

length = len(real_numbers)

if length == 1:
   arg = []
   num = int(real_numbers[0])
   n = 0.0
   for i in range(num):
       arg.append(n)
       n = n + 1
    
   formatted_tuple = tuple(arg)
   print(formatted_tuple)

elif length == 2:
    start = real_numbers[0]
    end = real_numbers[1]
    step = 1.0
    arg = []
    while start < end:
        arg.append(round(start, 3))
        start += step
    formatted_tuple = tuple(arg)
    print(formatted_tuple)       

elif length == 3:
    start = real_numbers[0]
    end = real_numbers[1]
    step = real_numbers[2]
    arg = []
    while start < end:
        arg.append(round(start, 3))
        start += step
    formatted_tuple = tuple(arg)
    print(formatted_tuple)       
    



   
