__author__ = 'taztony2010'

'''
Chapter 8 Practice Problem from Automate The Boring Stuff with
Python Copied the code directly out of book for learning purposes

Usage:  py.exe mcb.pym save <keyword> - Saves clipboard to keyword
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
        py.exe mcb.pyw list - Loads all the keywords to the clipboard
'''

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()