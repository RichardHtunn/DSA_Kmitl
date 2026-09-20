"""
Question 2: The Condo Parking Rearrangement (Doubly Linked List)

Lab Concepts Tested: Pointer integrity (Ch 5 Ex 2), Searching and arbitrary deletion (Ch 3 Ex 5 / Ch 5 Ex 1).

Problem Statement:
The parking alley at The Trendy Condo is so narrow that it operates as a Doubly Linked List.
Cars are represented by their license plate integers.

    Arrive <plate>: A car parks at the back (tail) of the alley.

    Depart <plate>: A specific car needs to leave. You must find it, remove it,
    and reconnect the prev and next pointers of the surrounding cars so the alley remains intact.

Process a string of commands. After processing, you must print the parking alley forwards
AND backwards to prove you did not break any prev or next pointers during deletion.
"""

class Node:
    def __init__(self, plate):
        self.plate = plate
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def arrive(self, plate):
        new_node = Node(plate)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def depart(self, plate):
        current = self.head
        while current:
            if current.plate == plate:
                # Handle Head deletion
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    
                # Handle Tail deletion
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                    
                return True # Successfully departed
            current = current.next
        return False # Car not found

    def print_forward(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.plate))
            curr = curr.next
        return " -> ".join(res) if res else "Empty"

    def print_backward(self):
        curr = self.tail
        res = []
        while curr:
            res.append(str(curr.plate))
            curr = curr.prev
        return " -> ".join(res) if res else "Empty"

def parking_simulator():
    commands = input("Enter Parking Commands: ").split(',')
    dll = DoublyLinkedList()
    
    for cmd in commands:
        action, plate = cmd.strip().split()
        if action == "Arrive":
            dll.arrive(plate)
        elif action == "Depart":
            dll.depart(plate)
            
    print(f"Forward: {dll.print_forward()}")
    print(f"Backward: {dll.print_backward()}")

if __name__ == '__main__':
    parking_simulator()