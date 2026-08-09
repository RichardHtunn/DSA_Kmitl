"""
Question 1: The Canteen Crush (Stack + Queue)

Lab Concepts Tested: Grouping logic (Ch 4 Ex 4), Consecutive Match/Explosion logic (Ch 4 Ex 5), LIFO vs FIFO.

Problem Statement:
During the lunch rush at the engineering faculty, students line up in a Queue. They are represented by
their department codes (e.g., 'C' for Computer, 'M' for Mechanical, 'E' for Electrical).

The cafeteria manager directs students from the front of the Queue into a narrow seating alley,
which acts as a Stack. To clear space quickly, if three students from the same department end up
seated next to each other at the top of the Stack, they are instantly moved to a VIP table (popped from the stack).

Write a program that takes a comma-separated string of department codes entering the Queue.
Process them into the Stack and trigger the "VIP clears" when 3 match.
Print the total number of VIP groups formed, and the remaining students in the seating Stack from bottom to top.
"""

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    def is_empty(self):
        return len(self.items) == 0

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def get_items(self):
        return self.items

def canteen_crush():
    user_input = input("Enter Student Queue: ").split(',')
    
    q = Queue()
    for student in user_input:
        q.enqueue(student.strip())
        
    seating_stack = Stack()
    vip_groups = 0
    
    while not q.is_empty():
        student = q.dequeue()
        seating_stack.push(student)
        
        # Check for "Crush" condition (3 identical consecutive departments)
        if seating_stack.size() >= 3:
            items = seating_stack.get_items()
            if items[-1] == items[-2] == items[-3]:
                # Move to VIP (Pop 3 times)
                seating_stack.pop()
                seating_stack.pop()
                seating_stack.pop()
                vip_groups += 1
                
    print(f"VIP Groups Formed: {vip_groups}")
    if seating_stack.is_empty():
        print("Seating Alley Empty")
    else:
        print(f"Remaining in Alley: {' -> '.join(seating_stack.get_items())}")

if __name__ == '__main__':
    canteen_crush()