# 6. For loops
s = 'Mihai'
for letter in s:
    print(letter)  # the print function is indented

for letter in s:
    print(letter, end='')  # prints entire string, although it iterates
print()  # without a new print, the next for loop print will continue to write
# in the first print; also, by default the print() has an '\n' default 'end' parameter
# print() has also the 'sep' paramater, which can work in combination with 'end'
for dog in s:
    if dog != 'i':
        print(dog, end='')
print()

# what will this print?
for i in range(len(s)):
    print(i, end='')
    #    print()
    print(s[i])

for i in range(len(s) - 1, -1, -1):
    print(s[i])

# While loops
x = 2
while x < 5:
    print('Ho')
    x += 1

