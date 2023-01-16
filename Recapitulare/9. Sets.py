"""
9. Sets
constructors - creating a new set
x = {3, 5, 3, 5}            # {5, 3}
x = set()                   # empty set
x = set(list1)              # new set from list, it strips duplicates

Set comprehension:
x = {3 * i for i in range(10) if i > 5}
resulting set: {24, 18, 27, 21}, order is random

Basic set operations
x.add(item)             # add item to set x
x.remove(item)          # remove item from set x
len(x)                  # get length of set x
item in x               # check membership in x
item not in x
x.pop()                 # pop random item from set x
x.clear()               delete all items from set x

Standard mathematical set operations
set1 & set2             AND                         intersection
set1 | set2             OR                          union
set1 ^ set2             XOR                         symmetric difference
set1 - set2             in set1 but not in set2     difference
set1 <= set2            set2 contains set1          subset
set1 >= set2            set1 contains set2          superset
"""
