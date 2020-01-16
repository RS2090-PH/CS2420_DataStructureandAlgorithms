# Pickling converts objects to text for storage without
# the programmer needing to manual convert everything

import pickle

lyst = [60, "A string object", 1977] # doesn't matter what's in the list
file_obj = open("items.dat", "wb") # opens file to be pickled. wb is write bits and rb is read bits 
for item in lyst:
    pickle.dump(item, file_obj) # dumping saves the selected item into the selected file object
file_obj.close()
