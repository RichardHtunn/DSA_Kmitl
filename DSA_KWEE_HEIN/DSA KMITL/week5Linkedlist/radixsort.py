class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail  = None
        self.length = 0

    def append(self,data):
        p = Node(data)
        # if empty or not
        if self.head:
            self.tail.next = p
            self.tail = p
            self.length += 1
        else:
            self.head = p
            self.tail = p
            self.length += 1

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def __str__(self):
        result = []
        current = self.head

        # Loop while a linked list exist
        while current:
            result.append(str(current.value))
            current = current.next

        return " -> ".join(result)

    def tospacestring(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " ".join(result)
    
def countdigit(num):
    return 1 if num == 0 else len(str(abs(num)))

def findmax(l):
    max_val = 0
    current = l.head
    while current:
        max_val = max(max_val, abs(current.value))
        current = current.next
    return max_val

def allEqual(l):
    if not l.head:
        return True
    value = l.head.value
    current = l.head.next
    while current:
        if current.value != value:
            return False
        current = current.next
    return True

def RadixSort(l):
    # find the max digit, it will be the time the sorting will be performed
    # after finding it, in range of max digit, perform radix sort
    before = str(l)
    if allEqual(l):
        max_digit = 0
    else:
        max_value = findmax(l)
        max_digit = countdigit(max_value)

        exponent = 1
        for r in range(1, max_digit +1):
            print("-" * 60)
            print(f"Round : {r}")

            pos_buckets = []
            # creating 10 empty linked lists
            for _ in range(10):
                pos_buckets.append(LinkedList())

            neg_buckets = []
            # creating 10 empty linked lists
            for _ in range(10):
                neg_buckets.append(LinkedList())
            
            current = l.head
            while current:
                digit = (abs(current.value) // exponent) % 10
                if current.value >= 0:
                    pos_buckets[digit].append(current.value)
                else:
                    neg_buckets[digit].append(current.value)
                current = current.next
            # print sorting steps inside 10 brackets
            for i in range(10):
                p_content = pos_buckets[i].tospacestring()
                n_content = neg_buckets[i].tospacestring()

                if p_content and n_content:
                    content = f"{p_content} {n_content}"
                elif p_content:
                    content = f"{p_content}"
                elif n_content:
                    content = f"{n_content}"
                else:
                    content = ""

                if content:
                    print(f"{i} : {content}")
                else:
                    print(f"{i} : ")

            # Rebuilding the list after rounds of sorting
            l = LinkedList()
            # handling positive side
            for i in range(9, -1, -1):
                current = pos_buckets[i].head
                while current:
                    l.append(current.value)
                    current = current.next

            # handling negative side
            for i in range(10):
                current = neg_buckets[i].head
                while current:
                    l.append(current.value)
                    current = current.next

            exponent *= 10
    print('-'*60)
    print(f"{max_digit} Time(s)")
    print(f"Before Radix Sort : {before}")
    print(f"After  Radix Sort : {str(l)} ")

if __name__ == "__main__":
    user_input = input("Enter Input : ")
    raw_values = [int(x) for x in user_input.split()]

    lst = LinkedList()
    for num in raw_values:
        lst.append(num)

    RadixSort(lst)