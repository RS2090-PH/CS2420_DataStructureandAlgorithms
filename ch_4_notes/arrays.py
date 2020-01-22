"""
File:arrays.py
An Array is like a list, but the client can use only [], len, iter, 
and str. To instantiate, use <variable>=Array(<capacity>,<optionalfillvalue>)
The fill value is None bydefault.
""" 
class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array. 
        fillValue is placed in each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """The capacity of the array."""
        return len(self.items)
    
    def __str__(self):
        """The string representation of the array."""
        return str(self.items)
    
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self,index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self,index,newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
    
def main():
    """Test code for Array class."""
    DEFAULT_CAPACITY = 5
    a = Array(DEFAULT_CAPACITY)
    logical_size = 0

    for rep in range(len(a)):
        a[rep] = rep + 1
        logical_size += 1

    if len(a) == logical_size:
        temp = Array(len(a) * 2)
        for rep in range(len(a)):
            temp[rep] = a[rep]
        a = temp
    
    print("Temp Array: ", temp)
    print("A Array: ", a)

    temp2 = Array(len(a) // 2)
    for rep in range(len(temp2)):
        temp2[rep] = a[rep]
        logical_size -= 1
    a = temp2

    a[2] = None
    logical_size = 2

    print("Temp Array: ", temp2)
    print("A Array: ", a)

    target_index = 1
    for rep in range(logical_size, target_index, - 1):
        a[rep] = a[rep - 1]
    a[target_index] = 10

    logical_size = 3
    print("A Array: ", a)

    target_index = 1
    for rep in range(target_index, logical_size - 1):
        a[rep] = a[rep - 1]
    logical_size -= 1

    print("A Array: ", a)


if __name__ == "__main__":
    main()
