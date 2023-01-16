"""
7. Lists
- most widely used data structure
- grow and shrink size as needed
- sequence type
- sortable

All operations from Sequences, plus:
- constructors:             x = list(), x = list(tuple1), x = ['a', 25, 8.3]
- del list1[2]              delete item from list1
- list1.append(item)        appends an item to list1
- list1.extend(sequence1)   appends a sequence to list1
- list1.insert(index, item) inserts item at index
- list1.pop()               pop last item
- list1.remove(item)        removes first instance of item
- list1.reverse()           reverses list order
- list1.sort()              sorts list in place

List comprehension:
x = [m for m in range(8)]  --> x = [0, 1, 2, 3, 4, 5, 6, 7]
x = [n**2 for n in range(10) if n > 4]  --> x = [25, 36, 49, 64, 81]

Delete: delete a list or an item from a list
x = [5, 3, 8, 6]
del(x[1])
del(x)

Append: append an item to a list
x.append(7)

Extend: extend a sequence to a list
y = [12, 13]
x.extend(y)

Insert: insert an item at given index
x.insert(1, 7)
x.insert(1, ['b', 'c'])

Pop: pops last item off the list, and returns item
x.pop()
print(x.pop())

Remove: remove first instance of an item
x = [5, 3, 8, 3, 4]
x.remove(3)

Reserve: reverse the order of the list
x.reverse()

Sort: sort the list in place without changing the original list
x.sort()
"""