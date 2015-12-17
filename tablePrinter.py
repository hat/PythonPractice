__author__ = 'taztony2010'

#This program takes a list of strings and displays it in a well organized table"

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0] * len(data)

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            colWidths[i] += len(data[i][j])

    #TODO longest_string should be longest word not total of lines
    longest_string = colWidths[0]

    for i in range(len(data[0])):
        for j in range(len(data)):
            if len(data[j][i]) > colWidths[j]:
                colWidths[j] = len(data[j][i])

    #TODO fix format to join each line and then print
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(8), end='')
        print()

printTable(tableData)