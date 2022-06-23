from pygame import Color
from math import floor
from enum import Enum

class PlayerColor(Enum):
    white = 1
    black = 2

class BoardPositionColor(Enum):
    white = 1
    black = 2


WIDTH = HEIGHT = 640
SQUARE_SIZE = HEIGHT/8

LETTER_POS_LABEL = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
}

def getNumberPositionByLetter(letter):
    return LETTER_POS_LABEL[letter]

def getLetterByNumberPosition(numberPosition):
    for k, v in LETTER_POS_LABEL.items():
        if v == numberPosition:
            return k

def getWorldPositionFromBoardPosition(boardPos):
    horizontalPos = getNumberPositionByLetter(boardPos[0]) * SQUARE_SIZE
    verticalPos = (8 - int(boardPos[1])) * SQUARE_SIZE
    return (horizontalPos, verticalPos)

def getBoardPositionFromWorldPosition(worldPos):
    letter = getLetterByNumberPosition(floor(worldPos[0]/ SQUARE_SIZE))
    num = 8 - floor(worldPos[1]/ SQUARE_SIZE )
    return f'{letter}{num}'

def getPygameColorByColor(color):
    if(color.name == 'white'):
        return Color('white')

    if(color.name == 'black'):
        return Color('grey')

def getFowardPosition(posLabel, amount=8, direction=1):
    possiblePositions = []
    horizontal = posLabel[0]
    vertical = int(posLabel[1])
    
    
    for x in range(amount):
        nextVertical = vertical + ((x + 1) * direction)
        if(nextVertical <= 8):
            possiblePositions.append(f'{horizontal}{nextVertical}')
    
    return possiblePositions

def getSidewaysPosition(posLabel, amount=8):
    possiblePositions = []
    row = posLabel[1]
    column = getNumberPositionByLetter(posLabel[0])
    for x in range(amount):
        nextColumn = column + x + 1
        if(nextColumn <= 9):
            possiblePositions.append(f'{getLetterByNumberPosition(nextColumn)}{row}')
     
    return possiblePositions