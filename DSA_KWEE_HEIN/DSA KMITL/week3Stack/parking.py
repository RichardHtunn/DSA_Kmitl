# two stacks of car parkings
# once have to remove temporarily, add the pop() one to the Mr.B stack
def CarPark(max, cars_input, op):
    stackA = []
    stackB = []
    cars_list = [int(x) for x in cars_input.split(",")]
    # debugger 
    # print(cars_list)
    for car in cars_list:
        stackA.append(car)
        # debuggger 
        # print(stackA)
    # do the parking process
    operator, car_num = op.split(" ")
    # debugger
    # print(operator)
    # print(car_num)
    car_num = int(car_num)
    # if car arrive
    if operator == 'arrive':
        # check the stack full by max or not
            if len(stackA) >= max:
                print(f"car {car_num} cannot arrive : Soi Full")
            # check the car_num is in stack or not
            elif car_num in stackA:
                print(f"car {car_num} already in soi")
            else:
                stackA.append(car_num)
                print(f"car {car_num} arrive! : Add Car {car_num}")
    elif operator == 'depart':
        # check the car exists in car_list
        while stackA and stackA[-1] != car_num:
            moved_car = stackA.pop()
            stackB.append(moved_car)
        if stackA and stackA[-1] == car_num:
            removed = stackA.pop()
            print(f"car {car_num} depart ! : Car {car_num} was remove")

        else:
            print(f"car {car_num} cannot depart : Dont Have Car {car_num}")
        while stackB:
            stackA.append(stackB.pop())
    return stackA

print("******** Parking Lot ********")
user_input = input("Enter max of car / car in soi / operation : ").split(" / ")
# debugging lines
max = int(user_input[0])
# print(max)
car = user_input[1]
# print(car)
op = user_input[2]
# print(op)
answer = CarPark(max, car, op)
print(answer)