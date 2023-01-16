# Sequences Theory
"""
Sequences - string, list, tuple:
- indexing                          x[3]
- slicing                           x[1:4]
- adding/concatenating              +
- multiplying                       *
- checking membership               in/not in
- iterating                         for i in x:
- len(string)
- min(string)
- max(string)
sum(string[1:3])
sorted(list1)
string.count(item)
string.index(item)

Indexing: access any item in the sequence using its index
string:
x = dog
print(x[1])  prints o

list:
x = ['cat', 'dog', 'horse']
print(x[1])  prints 'dog'

Slicing: slice out substrings, sublists, subtuples using indexes
[start:end+1:step]
x = 'computer'
x[1:4]    --> omp
x[1:6:2]  --> opt
x[3:]     --> puter
x[-1]     --> r
x[-3:]    --> ter
x[:-2]    --> comput

Adding/concatenating: combine 2 sequences of the same type using +
x = 'horse' + 'shoe'
print(x)  --> 'horseshoe'

x = ['pig', 'cow'] + ['horse']
print(x)  --> ['pig', 'cow', 'horse']

Multiplying: multiply a sequencte using *
x = 'cat' x 3
print(x)  --> 'catcatcat'

x = [3, 7] * 3
print(x)  --> [3, 7, 3, 7, 3, 7]

Checking membership: test whether an item is 'in' or 'not in' a sequence
x = 'cat'
print('a' in x)  --> prints True

x = ['pig', 'cow', 'horse']
print('cow' not in x)  --> prints False

Iterating: iterate through the items in a sequence
x = [3, 5, 2]
for item in x:
    print(item*2)   --> prints 6, 10, 4

x = [3, 5, 2]
for index, item in enumerate(x):
    print(index, item)  --> prints 0 3, 1 5, 2 2

Number of items: counts the number of items in a sequence
x = 'cat'
print(len(x))  --> prints 3

x = ['pig', 'cow', 'horse']
print(len(x))  --> prints 3

Minimum: find the minum item in a sequence lexicographically,
alpha or numeric types, but cannot mix them
x = 'cat'
print(min(x))  --> prints a

x = ['pig', 'cow', 'horse']
print(min(x))  --> prints 'cow'

Maximim: same as minimum, but with max

Sum: find the sum of items in a sequence, it needs to be numeric type
x = [5, 7, 2, 3]
print(sum(x))  --> prints 17
print(sum(x[-2:]))  --> prints 5

Sorting: returns a new list of items in sorted order,
does not change original list
x = 'cat'
print(sorted(x))   --> prints ['a','c','t']
x = ['pig', 'cow', 'horse']
print(sorted(x))  --> prints ['cow', 'horse', 'pig']

Index: returns the index of the first occurrence of an item
x = 'hippo'
print(index('p'))  --> prints 2

Unpacking: unpacks the n items of a sequence into n variables,
the number of variables must exactly match the length of the list
x = ['pig', 'cow', 'horse']
a, b, c = x  --> a = 'pig', b = 'cow', c = 'horse'
"""
