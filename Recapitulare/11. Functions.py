"""
11. Functions

A function is a block of statements that together perform an operation.
Any operation that is used often in a program can be split into its own function.

Function benefits:
- modularizes code
- easier to debug, reuse, maintain

def cuber(num=4):     # num = 2 is the default value
    num_cubed = num * num * num
    return num_cubed


# you also need to call the function and can pass an argument
x = 5
y = cuber()
cubed_x = cuber(x)
print(x, cubed_x, y)
"""
