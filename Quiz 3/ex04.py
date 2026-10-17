class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = int(size)
        self.max_col = int(max_col)
        self.threshold = int(threshold)

        if self.size <= 0:
            raise ValueError("table size must be positive")
        if self.max_col <= 0:
            raise ValueError("maximum collisions must be positive")
        if not 0 < self.threshold <= 100:
            raise ValueError("threshold must be between 1 and 100")

        self.table = [None] * self.size
        self.count = 0

    def insert(self, key, rehash=False):
        key = int(key)

        # Integer keys use set semantics: reinserting a key changes nothing.
        # This prevents impossible repeated rehashes for identical keys.
        if key in self.table:
            return False

        while True:
            if self._over_threshold(rehash):
                print("****** Data over threshold - Rehash !!! ******")
                self.rehash()
                continue

            if self._probe(key):
                return True

            print("****** Max collision - Rehash !!! ******")
            self.rehash()

    def _over_threshold(self, rehash=False):
        return not rehash and (self.count + 1) * 100 > self.threshold * self.size

    def _probe(self, key):
        for probe in range(self.max_col):
            index = (key + probe * probe) % self.size

            if self.table[index] is None:
                self.table[index] = key
                self.count += 1
                return True

            print(f"collision number {probe + 1} at {index}")

        return False

    def rehash(self):
        old_data = [item for item in self.table if item is not None]

        # Retry the complete saved data if migration itself hits the limit.
        # Use a loop rather than recursive rehash calls.
        while True:
            self.size = self._next_prime(self.size * 2)
            self.table = [None] * self.size
            self.count = 0

            # Reinsert in the old table's left-to-right order.
            for key in old_data:
                if not self._probe(key):
                    print("****** Max collision - Rehash !!! ******")
                    break
            else:
                return

    def _next_prime(self, n):
        candidate = n + 1

        while not self._is_prime(candidate):
            candidate += 1

        return candidate

    def _is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        divisor = 3

        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 2

        return True

    def is_full(self):
        return all(item is not None for item in self.table)

    def show(self):
        for index, item in enumerate(self.table, 1):
            print(f"#{index}\t{item}")
        print("----------------------------------------")


def main():
    print(" ***** Rehashing *****")

    try:
        config, data = input("Enter Input : ").split("/")
        size, max_col, threshold = map(int, config.split())
        hash_table = HashTable(size, max_col, threshold)

        print("Initial Table :")
        hash_table.show()

        for key in data.split():
            print("Add :", key)
            hash_table.insert(key)
            hash_table.show()
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
