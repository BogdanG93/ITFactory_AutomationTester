# 1. Variable
# Python variables : int, float, string, boolean, complex number

age = 18
first_name = 'Dragos'
price = 4.44

print('Age is type:', type(age))
print('"age" variable has the memory address:', id(age))
print(type(first_name))
print(type(price))

# type conversions: int(), float(), str(), bool(), hex(), ord() etc.

# naming can have letters, numbers and undersocre, it cannot start with a number
# some python reserved words cannot be used (eg. if, for, in etc.)
# use descriptive variable names ( first_name, age, weight etc.)
# Python is case sensitive (name !=Name)
# all variables in Python are reference variables --> it contains a
# memory address to where the data is stored ( use id() for address)
age = 22.5  # override
# Python uses 'dynamic typing' to check the changes
# when you override a variable it changes its memory address
# in Python most variables are immutable, meaning they don't change in-place
print('Age is now type:', type(age))
print('"age" variable has the memory address:', id(age))

x = 2
y = 15
x, y = y, x  # variables are swapped in one line of code
print('x=', x, 'y =', y)

# Boolean: True or False
# False: 0, 0.0, '', [], None, 1 and 0, 0 or "", 5-5, 3 < 1, -8 > 15
# 16 >= 100, 2 == 4, 3.5 != 3.5
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(None))
print(bool(1 and 0))
print(bool(0 or ''))
print(bool(5 - 5))

# True: any non-zero number, non-empty string, non-empty list
# 1, 1 or 0, -5 < 3, 6>=6, 2 == 2, 1.2 != 5, 8 > 5 and 12, 3 == 4 or [0]
print(bool(1))
print(bool(1 or 0))
print(bool(-5 < 3))
print(bool(4 == 4))
print(bool(4 and 3))
print(bool(2 == 4 or [0]))