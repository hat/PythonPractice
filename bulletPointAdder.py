__author__ = 'taztony2010'

'''
From Chapter 6 of Automate The Boring Stuff with Python
Copied the code directly out of book for learning purposes

This returns the the text that is copied on the clipboard
with a * before every newline
'''

import pyperclip
text = pyperclip.paste()

#TODO seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)