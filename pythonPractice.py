__author__ = 'taztony2010'

# testing basic math functions

print(3 + 5)
print(2 * 3)
print(2 ** 3)
print(5 - 2)
print(12 / 6)
print(15 // 7)
print(24 % 3)

# testing basic string functions

print('Enter your name: ')
name = raw_input()
print('Hello ' + str(name) + ' your name has a total of ' + str(len(name)))
print(name * 4)

# testing boolean conditions

date = ''

while date != 'the date':
    print('Enter the date: ')
    date = raw_input()
    if date == 'the':
        print('So close...')
        continue # jumps back to beginning of loop
    elif date == 'date':
        print('not quite')
    else:
        print('Great!')
        break # exits the loop



