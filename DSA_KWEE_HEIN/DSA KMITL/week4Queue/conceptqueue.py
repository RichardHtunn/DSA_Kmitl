# enqueue - add
# dequeue - reduce
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
        self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    

def ConceptQ(items):
    # let's split the op and num first
    q0 = Queue()
    dcounter = 0
    icounter = 0
    next_num = 0
    for item in items:
        print(f"Step : {item}")
        op = item[0]
        num = item[1:]
        # depent on op,  
        if op == "D":
            # check the q0 empty or not first
            if q0.isEmpty():
                error = int(num)
                dcounter += error
            else: 
                for i in range(int(num)):
                    if not q0.isEmpty():
                        q0.dequeue()
                    else:
                        dcounter += 1
            
            print(f"Dequeue : []")
            print(f"Error Dequeue : {dcounter}")
            print(f"Error input : {icounter}")
        elif op == "E":
            # check if the queue is empty, let's print with loop from num or not, continue from the existing
            for i in range(int(num)):
                q0.enQueue(next_num)
                next_num += 1
            
            print(f"Enqueue : {q0}")
            print(f"Error Dequeue : {dcounter}")
        
            print(f"Error input : {icounter}")
        else:
            icounter += 1
            print(f"{q0}")
            print(f"Error Dequeue : {dcounter}")
            print(f"Error input : {icounter}")
    
        print("--------------------")    
user_input = input("input : ").split(',')
answer = ConceptQ(user_input)
