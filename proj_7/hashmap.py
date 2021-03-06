"""
Author: Robby Stohel
File: hashmap.py

A hashmap program to store key/value sets.
"""

class HashMap():    # 'object' removed based on pylint recommendation
    """ Class to manage hashmap contents. """
    def __init__(self, cap=8):
        """ Initializes the class. """
        self.cap = cap
        self.itemct = 0
        self.hashmap = list()
        self.top_entries = list()
        for count in range(0, 15):
            self.top_entries.append(Entry())
        for item in range(0, self.cap):
            self.hashmap.append(Entry())

    def __iter__(self):
        """ Allows hashmap to be iterable. """
        return iter(self.hashmap)

    def __getitem__(self, item):
        """ Allows hashmap indexing. """
        return self.hashmap[item]

    def get(self, key, default=None):
        """ Locates and returns value of desired key. """
        for item in self.hashmap:
            if item.key() == key:
                return item.value()

        return default

    def set(self, key, value):
        """ Inserts a key/value pair into the hashmap if not
        initially present. Updates otherwise. """
        temp_index = self.key_to_index(key)
        flag = self.replace(key, value)

        if flag == 0:

            if self.hashmap[temp_index].key() is not key \
                and self.hashmap[temp_index].key() != "EMPTY":
                while flag != 1:
                    if self.hashmap[temp_index].key() is key \
                        or self.hashmap[temp_index].key() == "EMPTY":
                        if self.hashmap[temp_index].key() != key:
                            self.itemct += 1
                        self.hashmap[temp_index].ekey = key
                        self.hashmap[temp_index].evalue = value

                        flag += 1
                    if temp_index == (self.cap - 1):
                        temp_index = 0
                    else:
                        temp_index += 1

            else:
                self.hashmap[temp_index].ekey = key
                self.hashmap[temp_index].evalue = value
                self.itemct += 1

            if self.ld_factor() >= 0.8:
                self.rehash()


    def contains(self, check):
        """ Checks if a key is present in the hashmap. """
        for item in self.hashmap:
            if item.key() == check:
                return True
        return False

    def replace(self, check, replace):
        """ Finds a specific key and replaces its value. """
        for item in self.hashmap:
            if item.key() == check:
                item.evalue = replace
                return 1
        return 0

    def clear(self):
        """ Clears current hashmap. """
        self.cap = 8
        self.hashmap = list()

    def size(self):
        """ Provides current size of hashmap. """
        return self.itemct

    def capacity(self):
        """ Provides the current capacity. """
        return self.cap

    def keys(self):
        """ Creates a list containing all the keys present. """
        temp = list()
        for item in self.hashmap:
            if item.key() != "EMPTY":
                temp.append(item.key())
        return temp

    def values(self):
        """ Creates a list containing all the values present. """
        temp = list()
        for item in self.hashmap:
            if item.key() != "EMPTY":
                temp.append(item.value())
        return temp

    def ld_factor(self):
        """ Determines the current load factor. """
        return self.size()/self.cap

    def key_to_index(self, key):
        """ Converts the hash key into an index value. """
        return (abs(hash(key)) % self.cap) - 1

    def rehash(self):
        """ Rehashes the hashmap when the load is too high. """
        temp = HashMap(self.cap * 2)
        self.cap += self.cap

        for item in self.hashmap:
            if item.key() != "EMPTY":
                temp.set(item.key(), item.value())

        self.hashmap = temp.hashmap
        self.itemct = temp.itemct

    def top_fifteen(self):
        """ Produces a Top 15 list for value count. """
        temp = self.keys()

        for entry in temp:
            if self.get(entry) > self.top_entries[14].value():
                self.top_entries[14].ekey = entry
                self.top_entries[14].evalue = self.get(entry)
                self.top_entries.sort(reverse=True, key=(lambda kv: (kv[1], kv[0])))

    def print_top(self):
        """ Prints the Top 15 list. """
        self.top_fifteen()
        print("The most common words are:")
        for item in self.top_entries:
            print("%-8s         %-5d"%(item.key(), item.value()))

class Entry():    # 'object' removed based on pylint recommendation
    """ Class to organize individual entries. """
    def __init__(self, key="EMPTY", value=0):
        """ Initializes the class. """
        self.ekey = key
        self.evalue = value

    def __str__(self):
        """ Sets entry up for printing. """
        return "{'%s','%s'}"%(self.ekey, self.evalue)

    def __eq__(self, other):
        """ Allows entry value equal-to comparison. """
        if type(self.evalue) != type(other):
            return False
        return self.evalue == other

    def __lt__(self, other):
        """ Allows entry value less-than comparison. """
        if type(self.evalue) != type(other):
            return False
        return self.evalue < other

    def __gt__(self, other):
        """ Allows entry value greater-than comparison. """
        if type(self.evalue) != type(other):
            return False
        return self.evalue > other

    def __getitem__(self, item):
        """ Allows entry key/value indexing. """
        if item == 0:
            return self.ekey
        elif item == 1:
            return self.evalue

    def value(self):
        """ Allows value retrieval. """
        return self.evalue

    def key(self):
        """ Allows key retrieval. """
        return self.ekey
