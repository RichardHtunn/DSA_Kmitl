class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"


class Hash:
    def __init__(self, size, max_collision):
        self.size = int(size)
        self.max_collision = int(max_collision)

        if self.size <= 0:
            raise ValueError("table size must be positive")
        if self.max_collision <= 0:
            raise ValueError("maximum collisions must be positive")

        self.table = [None] * self.size
        self.table_full_shown = False

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def is_full(self):
        return all(item is not None for item in self.table)

    def display(self):
        for index, item in enumerate(self.table, 1):
            print(f"#{index}\t{item}")
        print("---------------------------")

    def insert(self, data):
        if self.is_full():
            if not self.table_full_shown:
                print("This table is full !!!!!!")
                self.table_full_shown = True
            return False

        original_index = self.hash_function(data.key)

        # Stop immediately upon the max_collision-th occupied slot.
        for probe in range(self.max_collision):
            index = (original_index + probe * probe) % self.size

            if self.table[index] is None:
                self.table[index] = data
                self.display()
                return True

            print(f"collision number {probe + 1} at {index}")

        print("Max of collisionChain")
        self.display()
        return False


def main():
    print(" ***** Fun with hashing *****")

    try:
        params, data = input("Enter Input : ").split("/")
        table_size, max_collision = params.split()
        hash_table = Hash(table_size, max_collision)

        if data.strip():
            for item in data.split(","):
                key, value = item.split()
                hash_table.insert(Data(key, value))
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
