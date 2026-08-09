User_input = input("Enter Input : ").split(",")
Speration = []
for i in User_input:
    sperate = i.strip().split(" ")
    Speration.append(sperate)

queue = []
num = 0
for j in Speration:
    action = j[0]
    if action == "E":
        value = j[1]
        queue.append(value)
        print(f"Add {value} index is {len(queue) - 1}")
        num += 1
    elif action == "D":
        if len(queue) > 0:
            removed_value = queue.pop(0)
            print(f"Pop {removed_value} size in queue is {len(queue)}")
        else:
            print("-1")

if len(queue) > 0:
    print(f"Number in Queue is :  {queue}")
else:
    print("Empty")




