__author__ = 'taztony2010'

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotatePicClockwise(pic):
    for i in range (len(pic[0])):
        for j in range (len(pic)):
            print(pic[j][i], end='')
        print()

rotatePicClockwise(grid);