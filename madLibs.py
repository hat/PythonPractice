__author__ = 'taztony2010'

toFillStory = open('madLib.txt', 'r') #the madlib
filledStory = open('madLibStory.txt', 'w') #finished madlib
newStory = '' #the finished madlib
punctuation = False #bool for period

'''
    This function takes a file of strings and splits it into words
'''
def words(fileObj):
    for line in fileObj:
        for word in line.split():
            yield word

'''
    This function gets a word from user input
'''
def getNewWord(word):
    new_word = input('Fill with a ' + word + ': ')
    return new_word

'''
    This function checks to see if a word is a part of speech
'''
def isPartOfSpeech(word):
    if word == 'ADJECTIVE' or word == 'NOUN' or word == 'ADVERB' or word == 'VERB':
        return True;

wordList = words(toFillStory) #holds the words from the file

#goes through each word of file
for word in wordList:
    #TODO check for commas etc...
    #checks if word is attached to period
    if word[-1] == '.':
        splitWord = word.split('.')
        #checks if split word is part of speech
        if (isPartOfSpeech(splitWord[0])):
            word = getNewWord(splitWord[0])
            punctuation = True
    #gets new word if word is part of speech
    elif isPartOfSpeech(word):
        word = getNewWord(word)

    #adds word to newstory
    newStory += word;

    #adds period back
    if punctuation:
        newStory += '.'
        punctuation = False

    #adds space between each word
    newStory += ' '

#prints the story to a new file
filledStory.write(newStory)