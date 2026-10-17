"""
Question 3: The VIM Editor with Undo History (Doubly Linked List + Stack)

Lab Concepts Tested: Cursor manipulation (Ch 5 Ex 4), Storing historical states (Ch 3).

Problem Statement:
Take the VIM Editor you built using a Doubly Linked List (where a cursor moves left/right and
you can Insert, Delete, or Backspace).

Add a new command: U (Undo).
To achieve this, you must use a Stack to record the state of the text every single time an action modifies the list
(I, D, or B). If U is called, pop the most recent state from the stack and restore the editor to that state.

Hint: Storing a deep copy of the Linked List in the stack is complex; instead, store a string representation
of the text and cursor state in the stack, and rebuild the Linked List when undoing.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class VIMEditor:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor_left = None
        self.history = [] # Acts as our Stack

    def save_state(self):
        # Push the current string state to the history stack BEFORE changing it
        self.history.append(str(self))

    def restore_state(self, state_str):
        # Clears the current DLL and rebuilds it from the saved string state
        self.head = self.tail = self.cursor_left = None
        if state_str == "|":
            return
            
        parts = state_str.split(' ')
        for part in parts:
            if part == '|':
                # The cursor is right after the last inserted node
                self.cursor_left = self.tail 
            else:
                self.insert_no_save(part)

    def insert_no_save(self, word):
        # Helper for rebuilding state without triggering another save
        new_node = Node(word)
        if self.cursor_left is None:
            new_node.next = self.head
            if self.head: self.head.prev = new_node
            self.head = new_node
            if self.tail is None: self.tail = new_node
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

    def insert(self, word):
        self.save_state()
        self.insert_no_save(word)

    def left(self):
        if self.cursor_left is not None:
            self.cursor_left = self.cursor_left.prev

    def right(self):
        if self.cursor_left is None:
            if self.head is not None:
                self.cursor_left = self.head
        else:
            if self.cursor_left.next is not None:
                self.cursor_left = self.cursor_left.next

    def backspace(self):
        if self.cursor_left is not None:
            self.save_state()
            to_delete = self.cursor_left
            prev_node = to_delete.prev
            next_node = to_delete.next
            if prev_node: prev_node.next = next_node
            else: self.head = next_node
            if next_node: next_node.prev = prev_node
            else: self.tail = prev_node
            self.cursor_left = prev_node

    def undo(self):
        if self.history:
            previous_state = self.history.pop()
            self.restore_state(previous_state)

    def __str__(self):
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
    inp = input("Enter VIM Commands (e.g., I Hello, I World, L, B, U): ")
    editor = VIMEditor()
    
    for cmd in inp.split(','):
        cmd = cmd.strip()
        if not cmd: continue
            
        if cmd.startswith('I'):
            editor.insert(cmd.split(' ', 1)[1])
        elif cmd == 'L': editor.left()
        elif cmd == 'R': editor.right()
        elif cmd == 'B': editor.backspace()
        elif cmd == 'U': editor.undo()
            
    print(f"Final Editor State: {editor}")
