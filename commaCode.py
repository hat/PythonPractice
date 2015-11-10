__author__ = 'taztony2010'

spam = ['apples', 'bananas', 'tofu', 'cats', 'frog'];

def printList(items):

    fullList = '';

    for word in items:
        if( word != items[len(items) - 1] ):
            fullList += word + ', ';
        else:
            fullList += 'and ' + word;
    return fullList;

print(printList(spam));