"""
10. Dictionaries

constructors - creating a new dict
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
x = dict(pork=25.3, beef=33.8, chicken=22.7)

Basic dict operations
x['beef'] = 25.2            add or change item in dict x
del x['beef']               remove item from dict x
len(x)                      get length of dict x
item in x                   check membership in x
item not in x               (only looks in keys, not values)
x.clear()                   delete all items from dict x
del x                       delete dict x

Accessing keys and values in a dict
x.keys()                    returns list of keys in x
x.values()                  returns list of values in x
x.items()                   returns list of key-value tuple pairs in x
item in x.values()          test membership in x: returns boolean

Iterating in a dict
for key in x:               iterate keys
    print(key, x[key]       print all key/value pairs

for k, v in x.items():      iterate key/value pairs
    print(k, v)             print all key/value pairs
"""
