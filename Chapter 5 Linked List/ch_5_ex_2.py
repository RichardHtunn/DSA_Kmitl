class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        """Initializes the linked list."""
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        """Returns whether the list is empty."""
        return self.head is None

    def __str__(self):
        """Returns a string representing the values in the linked list."""
        if self.isEmpty():
            return ""
        
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += "->"
            current = current.next
        return result

    def str_reverse(self):
        """Returns a string representing the values in the linked list from back to front."""
        if self.isEmpty():
            return ""
            
        current = self.tail
        result = ""
        while current is not None:
            result += str(current.data)
            if current.previous is not None:
                result += "->"
            current = current.previous
        return result

    def append(self, data):
        """Adds a node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, index, data):
        """Inserts data at the specified index."""
        if index < 0 or index > self.size:
            return False
            
        if index == 0:
            new_node = Node(data)
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
            self.size += 1
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index):
                current = current.next

            previous_node = current.previous
            
            previous_node.next = new_node
            new_node.previous = previous_node
            
            new_node.next = current
            current.previous = new_node
            
            self.size += 1
        return True

    def remove(self, data):
        """Removes and returns the node with the given data."""
        current = self.head
        
        while current is not None:
            if current.data == data:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next 
                    
                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                    
                self.size -= 1

                current.next = None
                current.previous = None
                return current
                
            current = current.next

        return None


if __name__ == '__main__':
    ll = DoublyLinkedList()
    user_input = input("Enter Input : ")
    commands = user_input.split(',')
    
    for cmd_string in commands:
        cmd_string = cmd_string.strip()
        if not cmd_string:
            continue
            
        parts = cmd_string.split(' ', 1)
        cmd = parts[0].strip()
        
        if cmd == 'A':
            data = parts[1].strip()
            ll.append(data)
            
        elif cmd == 'Ab':
            data = parts[1].strip()
            ll.insert(0, data)
            
        elif cmd == 'I':
            idx, data = parts[1].split(':')
            idx = int(idx.strip())
            data = data.strip()
            
            if idx < 0 or idx > ll.size:
                print("Data cannot be added")
            else:
                print(f"index = {idx} and data = {data}")
                ll.insert(idx, data)
            
        elif cmd == 'R':
            data = parts[1].strip()

            current = ll.head
            idx = 0
            found = False
            
            while current is not None:
                if current.data == data:
                    found = True
                    break
                current = current.next
                idx += 1
                
            if not found:
                print("Not Found!")
            else:
                ll.remove(data)
                print(f"removed : {data} from index : {idx}")
            
        print(f"linked list : {ll}")
        print(f"reverse : {ll.str_reverse()}")