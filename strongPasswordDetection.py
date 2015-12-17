__author__ = 'taztony2010'

'''
Chapter 8 Practice Problem from Automate The Boring Stuff with
Python Copied the code directly out of book for learning purposes

This program uses regex to make sure a password is at least eight characters long,
contains both uppercase and lowercase characters, and at least one digit.
'''

import re

lengthRegex = re.compile('.{8}')
capitalRegex = re.compile('[A-Z]')
lowerRegex = re.compile('[a-z]')
digitRegex = re.compile('\d')

passwordRegex = re.compile(r'''(
    (?=.{8})              #8 characters
    ^(?= .*[A-Z].*[A-Z])  #2 Capital Letters
    (?= .*[a-z].*[a-z])   #2 lower case letters
    (.{1,})               #one digit
)''', re.VERBOSE)

def checkPassword():
    password = input('Enter a password: ')
    check = passwordRegex.search(password)
    if( not check ):
        print('Your password does not meet the requirements')
        return False
    else:
        print('Perfect, no one will be able to guess that')
        return True

checkPassword()
