def run_parking_lot():
    print("******** Parking Lot ********")
    user_input = input("Enter max of car / car in soi / operation : ")
    
    parts = user_input.split('/')
    max_capacity = int(parts[0].strip())
    cars_str = parts[1].strip()
    
    action_parts = parts[2].strip().split()
    action = action_parts[0]
    target_car = int(action_parts[1]) 

    alley_a = []
    if cars_str != "":
        alley_a = [int(x.strip()) for x in cars_str.split(',')]
            
    alley_b = []
    
    if action == "arrive":
        if target_car in alley_a:
            print(f"car {target_car} already in soi")
        elif len(alley_a) >= max_capacity:
            print(f"car {target_car} cannot arrive : Soi Full")
        else:
            alley_a.append(target_car)
            print(f"car {target_car} arrive! : Add Car {target_car}")
            
    elif action == "depart":
        if not alley_a:
            print(f"car {target_car} cannot depart : Soi Empty")
        elif target_car not in alley_a:
            print(f"car {target_car} cannot depart : Dont Have Car {target_car}")
        else:
            while alley_a:
                popped_car = alley_a.pop()
                if popped_car == target_car:
                    print(f"car {target_car} depart ! : Car {target_car} was remove")
                    break 
                else:
                    alley_b.append(popped_car) 
            
            while alley_b:
                alley_a.append(alley_b.pop())
                
    print(alley_a)

run_parking_lot()