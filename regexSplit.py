__author__ = 'taztony2010'

import re

#TODO EVERYTHING!!!!!!

def regexStrip(string, c):
    regex = r'''^[' + chars + ']+|[' + chars + ']+$'''
    strip = re.compile(regex)
    print(strip.search(string))

regexStrip('hello there', 'h')

