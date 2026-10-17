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


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items


def play_color_crush_2():
    user_input = input("Enter Input (Normal, Mirror) : ")
    normal_str, mirror_str = user_input.split()

    mirror_reversed = mirror_str[::-1]
    
    mirror_stack = Stack()
    mirror_queue = Queue()
    mirror_explosions = 0
    
    for char in mirror_reversed:
        mirror_stack.push(char)
        
        if mirror_stack.size() >= 3:
            items = mirror_stack.get_items()
            if items[-1] == items[-2] == items[-3]:
                exploded_char = items[-1]
                mirror_stack.pop()
                mirror_stack.pop()
                mirror_stack.pop()
                
                mirror_queue.enqueue(exploded_char)
                mirror_explosions += 1

    normal_stack = Stack()
    normal_explosions = 0
    failed_interruptions = 0
    
    for char in normal_str:
        normal_stack.push(char)
        
        if normal_stack.size() >= 3:
            items = normal_stack.get_items()
            if items[-1] == items[-2] == items[-3]:
                
                if not mirror_queue.is_empty():
                    block_item = mirror_queue.dequeue()
                    
                    if block_item == items[-1]:
                        normal_stack.pop()
                        normal_stack.pop()
                        failed_interruptions += 1
                    else:
                        top = normal_stack.pop()
                        normal_stack.push(block_item)
                        normal_stack.push(top)
                
                else:
                    normal_stack.pop()
                    normal_stack.pop()
                    normal_stack.pop()
                    normal_explosions += 1

    print("NORMAL :")
    print(normal_stack.size())
    if normal_stack.is_empty():
        print("Empty")
    else:
        print("".join(reversed(normal_stack.get_items())))
        
    print(f"{normal_explosions} Explosive(s) ! ! ! (NORMAL)")
    
    if failed_interruptions > 0:
        print(f"Failed Interrupted {failed_interruptions} Bomb(s)") 

    print("------------MIRROR------------")
    print(": RORRIM")
    print(mirror_stack.size())
    if mirror_stack.is_empty():
        print("ytpmE")
    else:
        print("".join(reversed(mirror_stack.get_items())))
        
    print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_explosions}")

if __name__ == '__main__':
    play_color_crush_2()