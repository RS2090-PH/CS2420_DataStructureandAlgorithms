"""
File: hashtable.py

Case study for Chapter 11.
"""

from arrays import Array

class HashTable(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29,
                 hashFunction = hash,
                 linear = True):
        self.table = Array(capacity, HashTable.EMPTY)
        self.size = 0
        self.hash = hashFunction
        self.homeIndex = -1
        self.actualIndex = -1
        self.linear = linear
        self.probeCount = 0
        self.capacity = capacity

    def __str__(self): #FIXME: Complete this
        temp = "["
        count = 0

        for item in self.table:
            if count == 0:
                temp = temp + str(item)
                count += 1
            else:
                temp = temp + ", " + str(item)
        temp = temp + "]"

        return temp

    def __len__(self):
        return self.size

    def getLoadFactor(self):
        return (self.size / self.capacity)

    def getHomeIndex(self):
        return self.homeIndex

    def getActualIndex(self):
        return self.actualIndex

    def getProbeCount(self):
        return self.probeCount

    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self.probeCount = 0
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex

        # Stop searching when an empty cell is encountered
        while not self.table[index] in (HashTable.EMPTY,
                                        HashTable.DELETED):

            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
            index = increment % len(self.table)
            self.probeCount += 1

        # An empty cell is found, so store the item
        self.table[index] = item
        self.size += 1
        self.actualIndex = index

    # Methods __len__(), __str__(), getLoadFactor(), getHomeIndex(),
    # getActualIndex(), and getProbeCount() are exercises.
    def get(self, item): #FIXME: Complete this part
        self.probeCount = 0
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex
        checked = 0

        # Stop searching when an empty cell is encountered
        while self.table[index] != item:
            if checked == self.probeCount:
                return -1
            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
                checked += 1
            index = increment % len(self.table)
            self.probeCount += 1

        return index

    def remove(self, item): #FIXME: Complete this part
        self.probeCount = 0
        # Get the home index
        self.homeIndex = abs(self.hash(item)) % len(self.table)
        distance = 1
        index = self.homeIndex
        checked = 0

        # Stop searching when an empty cell is encountered
        while self.table[index] != item:
            if checked == self.capacity:
                return -1
            # Increment the index and wrap around to first 
            # position if necessary
            if self.linear:
                increment = index + 1
                checked += 1
            else:
                # Quadratic probing
                increment = self.homeIndex + distance ** 2
                distance += 1
                checked += 1
            index = increment % len(self.table)
            self.probeCount += 1
        
        self.table[index] = self.DELETED
        self.size -= 1

        return index
        
def main():
    """Uses an example data set from Chapter 19."""
    #table = HashTable(8, lambda x : x)
    #for item in (range(10, 71, 10)):
    #    table.insert(item)
    #    print("Home:", table.getHomeIndex(), "Probes:", table.getProbeCount(),
    #          "Load factor:", table.getLoadFactor())
    #    print(table)

    table = HashTable(8, lambda x: x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    print("Result: ",table.remove(10))
    print("Expects: 2")
    print("Result: ", str(table) )
    print("Expects: [40, None, True, 50, 20, 60, 30, 70]")
    print("Result: ",table.remove(60))
    print("Expects: 5")
    print("Result: ", str(table))
    print("Expects: [40, None, True, 50, 20, True, 30, 70]")

if __name__ == "__main__":
    main()
