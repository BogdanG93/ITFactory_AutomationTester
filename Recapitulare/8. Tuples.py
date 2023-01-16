"""
8. Tuples
- support all operations for Sequences
- immutable, but member objects may be mutable
- if the contents of a list shouldn't change, use a tuple to prevent
  items from accidentally being added, changed or deleted
- tuples are more efficient than lists due to Python's implementation

Creating a new tuple:

x = ()                  # no-item tuple
print(type(x))

x = (1, 2, 3)
print(type(x))

x = 1, 2, 3             # paranthesis are optional

x = 2,                  # single-item tuple
print(type(x))

list1 = [1, 2, 3]
x = tuple(list1)        # tuple from list
print(type(x))

Tuples are immutable, but objects may be mutable
x = (1, 2, 3)
del(x[1])           # error!
x[1] = 8            # error!
x = ([1, 2], 3)     # 2-tem tuple: list and int
del(x[0][1])        # ([1], 3)
"""