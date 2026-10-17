class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def insert(self, index, item):
        self.items.insert(index, item)

    def size(self):
        return len(self.items)
        
    def __getitem__(self, index):
        return self.items[index]


def process_canteen_queue():
    user_input = input("Enter Input : ")
    
    # Split the input into employee data and operations
    employee_data, operations_data = user_input.split('/')
    
    # Create a dictionary to map Employee ID -> Department ID
    emp_to_dept = {}
    for entry in employee_data.split(','):
        dept_id, emp_id = entry.split()
        emp_to_dept[emp_id] = dept_id
        
    q = Queue()

    operations = operations_data.split(',')
    for op in operations:
        if op == 'D':
            if q.is_empty():
                print("Empty")
            else:
                print(q.dequeue())
                
        elif op.startswith('E'):
            _, emp_id = op.split()
            dept_id = emp_to_dept.get(emp_id)
            
            insert_index = q.size() 
            
            for i in range(q.size() - 1, -1, -1):
                queued_emp_id = q[i]
                if emp_to_dept.get(queued_emp_id) == dept_id:
                    insert_index = i + 1
                    break
            
            q.insert(insert_index, emp_id)

if __name__ == '__main__':
    process_canteen_queue()