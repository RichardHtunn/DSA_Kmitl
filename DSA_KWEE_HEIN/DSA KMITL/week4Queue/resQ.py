# restaurant
class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items =[]
        else:
            self.items = list
    
    def __str__(self):
        return str([f"*{x}" for x in self.items])
    
    def enQueue(self,i ):
        self.items.append(i)
    
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

def resQ(items):
    staff_info = items[0]
    # print(staff_info)
    q0 = Queue()
    pairs = staff_info.split(",")
    dept = {}
    for pair in pairs:
        did,id = pair.strip().split()
        dept[id] = did
    # print(dept)
    op_info = items[1]
    pairs = op_info.split(",")
    for a in pairs:
        parts = a.strip().split(" ",1)
        op = parts[0]
        # debugger
        # print(op)
        num = parts[1] if len(parts) > 1 else None
        if op == "D" and num is None:
            # check if the q empty and return empty
            if q0.isEmpty():
                print("Empty")
            else:
                print(q0.dequeue())
        elif op == "E" and num is not None:
            new_dept = dept[num]
            insert = False

            # loop backward to check the same department staff exists or not
            n = q0.size()
            for i in range(n - 1, -1, -1):
                existing_staff = q0.items[i]
                if dept[existing_staff] == new_dept:
                    # append it right after the existing one
                    q0.items.insert(i+1 , num)
                    insert = True
                    break
            if not insert:
                q0.enQueue(num)


    return

user_input = input("Enter Input : ").split("/")
answer = resQ(user_input)