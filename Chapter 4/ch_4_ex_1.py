user_input = input("Enter Input : ").split(',')

queue = []

for items in user_input:
    parts = items.strip().split()

    if parts[0] == 'E':
        val = parts[1]
        queue.append(val)
        print(f"Add {val} index is {len(queue) - 1}")
    elif parts[0] == 'D':
        if len(queue) > 0:
            val = queue.pop(0)
            print(f"Pop {val} size in queue is {len(queue)}")
        else:
            print("-1")

if len(queue) > 0:
    print(f"Number in Queue is :  {queue}")
else:
    print("Empty")