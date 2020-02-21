"""
Define a recursive, Boolean function named equals for two Lisp-like
lists. Two lists are equal if they are both empty, or their lengths
are the same and their first items are equal and the rest of their
items are equal.

Here is an example of its use:

>>> from lisplist import *
>>> lyst = buildRange(1, 5)
>>> lyst
(1 2 3 4 5)
>>> equals(lyst, buildrange(1, 5))
True
>>> equals(lyst, buildrange(1, 4))
False
"""