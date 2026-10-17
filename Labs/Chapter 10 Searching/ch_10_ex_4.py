class hash:
    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * size
        self.data = []

    def is_prime(self, n):
        if n < 2:
            return False

        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1

        return True

    def rehash(self):
        previous = self.data[:]
        self.size = self.size * 2 + 1

        while not self.is_prime(self.size):
            self.size += 1

        self.table = [None] * self.size
        self.data = []

        for value in previous:
            self.insert(value)

    def insert(self, value):
        if (len(self.data) + 1) * 100 > self.threshold * self.size:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()

        collision = 0

        while True:
            index = (value % self.size + collision ** 2) % self.size

            if self.table[index] is None:
                self.table[index] = value
                self.data.append(value)
                return

            collision += 1
            print(f"collision number {collision} at {index}")

            if collision == self.max_collision:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                collision = 0

    def display(self):
        for i, value in enumerate(self.table, 1):
            print(f"#{i}\t{value}")
        print("----------------------------------------")


print(" ***** Rehashing *****")
config, values = input("Enter Input : ").split("/", 1)
size, max_collision, threshold = map(int, config.split())
table = hash(size, max_collision, threshold)

print("Initial Table :")
table.display()

for value in map(int, values.split()):
    print(f"Add : {value}")
    table.insert(value)
    table.display()