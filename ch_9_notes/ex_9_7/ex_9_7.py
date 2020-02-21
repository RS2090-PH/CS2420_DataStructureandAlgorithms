"""
Define a recursive function named insert, that expects an index, an
item, and a Lisp-like list as arguments. The function returns a list
in which the item is inserted at the given index position.

Here is an example of its use:

>>> from lisplist import *
>>> lyst = buildRange(1, 5)
>>> lyst
(1 2 3 4 5)
>>> insert(2, 66, lyst) # insert 66 at position 2
(1 2 66 3 4 5)
>>> lyst
(1 2 3 4 5)
"""