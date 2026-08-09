print("******** Parking Lot ********")
max_car, current_car, operation = input("Enter max of car / car in soi / operation : ").split("/")
max_car = int(max_car)
current_car = current_car.split(",")
operation = operation.strip().split(" ")
command = str(operation[0])
target_car = int(operation[-1])

car = []
for i in current_car:
    car.append(int(i))

soi_a = car
soi_b = []

if command == "arrive":
    if len(soi_a) >= max_car:
        print(f"car {target_car} cannot arrive : Soi Full")
    elif target_car in soi_a:
        print(f"car {target_car} already in soi")
    else:
        soi_a.append(target_car)
        print(f"car {target_car} arrive! : Add Car {target_car}")

elif command == "depart":
    if target_car not in soi_a:
        print(f"car {target_car} cannot depart : Dont Have Car {target_car}")
    else:
        while soi_a[-1] != target_car:
            block_car = soi_a.pop()
            soi_b.append(block_car)
        soi_a.pop()
        print(f"car {target_car} depart ! : Car {target_car} was remove")
        while len(soi_b) > 0:
            return_car = soi_b.pop()
            soi_a.append(return_car)

print(soi_a)

