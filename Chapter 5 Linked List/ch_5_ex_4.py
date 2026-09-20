class Node:
    """A node in the doubly linked list representing a single word."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class VIMEditor:
    """Doubly Linked List implementation of a simplified Text Editor."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor_left = None
        
    def insert(self, word):
        """Inserts the word at the current cursor position."""
        new_node = Node(word)
        if self.cursor_left is None:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            
            if self.tail is None:
                self.tail = new_node
                
            self.cursor_left = new_node
        else:
            new_node.next = self.cursor_left.next
            new_node.prev = self.cursor_left
            
            if self.cursor_left.next:
                self.cursor_left.next.prev = new_node
            else:
                self.tail = new_node
                
            self.cursor_left.next = new_node
            self.cursor_left = new_node

    def left(self):
        """Moves the cursor one position to the left."""
        if self.cursor_left is not None:
            self.cursor_left = self.cursor_left.prev

    def right(self):
        """Moves the cursor one position to the right."""
        if self.cursor_left is None:
            if self.head is not None:
                self.cursor_left = self.head
        else:
            if self.cursor_left.next is not None:
                self.cursor_left = self.cursor_left.next

    def backspace(self):
        """Deletes the character to the left of the cursor."""
        if self.cursor_left is not None:
            to_delete = self.cursor_left
            prev_node = to_delete.prev
            next_node = to_delete.next
            
            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node
                
            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node

            self.cursor_left = prev_node

    def delete(self):
        """Deletes the character to the right of the cursor."""
        node_to_delete = None
        if self.cursor_left is None:
            node_to_delete = self.head
        else:
            node_to_delete = self.cursor_left.next
            
        if node_to_delete is not None:
            prev_node = node_to_delete.prev
            next_node = node_to_delete.next
            
            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node
                
            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node

    def __str__(self):
        """String representation showing words and the cursor position."""
        result = []
        if self.cursor_left is None:
            result.append("|")
            
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            if curr == self.cursor_left:
                result.append("|")
            curr = curr.next
            
        return " ".join(result)

if __name__ == '__main__':
    inp = input("Enter Input : ")
    commands = inp.split(',')
    editor = VIMEditor()
    
    for cmd in commands:
        cmd = cmd.strip()
        if not cmd:
            continue

        if cmd.startswith('I'):
            parts = cmd.split(' ', 1)
            word = parts[1]
            editor.insert(word)
        elif cmd == 'L':
            editor.left()
        elif cmd == 'R':
            editor.right()
        elif cmd == 'B':
            editor.backspace()
        elif cmd == 'D':
            editor.delete()
            
    print(editor)