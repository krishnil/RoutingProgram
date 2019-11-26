# Create a hashtable with insert and lookup function for the Packages.
class HashTable:
    def __init__(self, capacity=41):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def hash_insert(self, package):
        bucket = package.id % len(self.table)
        self.table[bucket] = package

    def hash_search(self, key):
        bucket = key % len(self.table)
        if self.table[bucket] is not None:
            return self.table[bucket]
        else:
            return None
