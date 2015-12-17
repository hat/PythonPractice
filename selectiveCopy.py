__author__ = 'taztony2010'

'''selectiveCopy.py - Copies an entire folder and its contents into
   a zip file whose filename increments
'''

import shutil, os, re, sys

#First command line argument specifies file extension
#extension = sys.argv[1]

extension = '.txt'

#Create regex to search for all filename extensions
fileNamePattern = re.compile("""\.\w{2,} #find period followed by word
                                (\n|\t|\r) #makes sure it ends with newline tab or return
                            """, re.VERBOSE)

#run through all files
for filename in os.listdir('.'):
    #returns the extension
    fn = fileNamePattern.search(filename)

    #continues if no extension
    if fn == None:
        continue

    #if the extension matches the command line argument
    if(fn.group(0) == extension):
        print('Copying: ' + filename + ' to Users/taztony2010/Downloads/DELETE')
        print(os.getcwd() + '/' + filename)
        #Uncomment to move files to new folder
        #shutil.copy(os.getcwd() + '/' + filename, '/Users/taztony2010/Downloads/DELETE')