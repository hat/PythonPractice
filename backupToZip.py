__author__ = 'taztony2010'

'''beckupToZip.py - Copies an entire folder and its contents into
   a zip file whose filename increments

   Copied directly from chapter 9 of Automate the Boring Stuff With Python
'''

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a zip file
    folder = os.path.abspath(folder) #make sure the folder is absolute

    #Figure out the filename this code should use based on
    #what files already exist
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    #Create the zip file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    #Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #Add the current folder to the ZIP file
        backupZip.write(foldername)
        #Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    #don't back up the zip files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\Delicious')

