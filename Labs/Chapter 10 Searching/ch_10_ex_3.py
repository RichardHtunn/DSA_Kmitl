class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size
        self.count = 0

    def insert(self, data):
        base = sum(ord(c) for c in data.key) % self.size

        for collision in range(self.max_collision):
            index = (base + collision ** 2) % self.size

            if self.table[index] is None:
                self.table[index] = data
                self.count += 1
                return

            print(f"collision number {collision + 1} at {index}")

        print("Max of collisionChain")

    def display(self):
        for i, data in enumerate(self.table, 1):
            print(f"#{i}\t{data}")
        print("---------------------------")

    def is_full(self):
        return self.count == self.size


print(" ***** Fun with hashing *****")
config, entries = input("Enter Input : ").split("/", 1)
size, max_collision = map(int, config.split())
table = hash(size, max_collision)

for entry in entries.split(","):
    if table.is_full():
        print("This table is full !!!!!!")
        break

    key, value = entry.split()
    table.insert(Data(key, value))
    table.display()