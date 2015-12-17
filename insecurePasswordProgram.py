__author__ = 'taztony2010'

'''
From Chapter 6 of Automate The Boring Stuff with Python
Copied the code directly out of book for learning purposes

This program takes a command line argument and returns the password
'''

PASSWORDS = {'email': 'F7hgrjbHEJDhbrei743437',
             'blog': 'GHU7y37gDUHFu7&^',
             'luggage': '12345'}
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python insecurePasswordProgram.py [account]')
    sys.exit()

account = sys.argv[1] #first account line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)