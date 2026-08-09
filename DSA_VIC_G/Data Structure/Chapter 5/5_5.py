class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_Empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 

    def pop_head(self):
        if self.head == None:
            return None
        
        pop = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return pop

    def __str__(self):
        if self.head == None:
            return ""
        output = ""
        current = self.head
        while current != None:
            output += str(current.data)
            if current.next != None:
                output += " -> "
            current = current.next
        return output

#largest to smallest
def is_sorted(ll):
    cursor = ll.head
    if not cursor:
        return True
    while cursor.next:
        if cursor.data < cursor.next.data:
            return False
        cursor = cursor.next
    return True

User_input = input("Enter Input : ").split(" ")
ll = LinkedList()
max_digit = 0

for i in User_input:
    number = int(i)
    ll.append(number)
    if number != 0:
        length = len(str(abs(number)))
        if length > max_digit:
            max_digit = length

Changing_str = str(ll)
rounds = 0

#run as many rounds as longest digit
while rounds < max_digit:
    rounds += 1
    print("------------------------------------------------------------")
    print(f"Round : {rounds}")

    #create 10 empty buckets 0 to 9
    buckets = []
    for i in range(10):
        buckets.append(LinkedList())

    pos_list = LinkedList()
    neg_list = LinkedList()

    while not ll.is_Empty():
        value = ll.pop_head()
        if value >= 0:
            pos_list.append(value)
        else:
            neg_list.append(value)

    while not pos_list.is_Empty():
        value = pos_list.pop_head()
        str_value = str(abs(value))

        #checking if number is long enough for current round
        if rounds <= len(str_value):
            #take the charactor from right side
            digit_char = str_value[-rounds]
            digit = int(digit_char)
        else:
            digit = 0

        buckets[digit].append(value)

    while not neg_list.is_Empty():
        value = neg_list.pop_head()
        str_value = str(abs(value))

        #checking if number is long enough for current round
        if rounds <= len(str_value):
            #take the charactor from right side
            digit_char = str_value[-rounds]
            digit = int(digit_char)
        else:
            digit = 0

        buckets[digit].append(value)

    #output the bucket
    for i in range(10):
        b_str = ""
        current = buckets[i].head
        while current != None:
            b_str += str(current.data) + " "
            current = current.next
        print(f"{i} : {b_str}")

    #Positive (read buckets backward)
    for i in range(9, -1, -1):
        current = buckets[i].head
        while current != None:
            if current.data >= 0:
                ll.append(current.data)
            current = current.next

    #Negative (read buckets forward)
    for i in range(10):
        current = buckets[i].head
        while current != None:
            if current.data < 0:
                ll.append(current.data)
            current = current.next 

print("------------------------------------------------------------")
print(f"{rounds} Time(s)")
print(f"Before Radix Sort : {Changing_str}")
print(f"After  Radix Sort : {ll}") 