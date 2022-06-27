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
        if(nextVertical <= 8 and nextVertical >= 1):
            possiblePositions.append(f'{horizontal}{nextVertical}')
    
    return possiblePositions

def getSidewaysPosition(posLabel, amount=8, direction=1):
    possiblePositions = []
    horizontal = getNumberPositionByLetter(posLabel[0])
    vertical = posLabel[1]
    
    for x in range(amount):
        nextHorizontal = horizontal + ((x + 1) * direction)
        if(nextHorizontal <= 8 and nextHorizontal >= 1):
            possiblePositions.append(f'{getLetterByNumberPosition(nextHorizontal)}{vertical}')
     
    return possiblePositions

def getDiagonalPosition(posLabel):
    possiblePositions = []
    directionsPairs = [(1,1), (1, -1), (-1, 1), (-1, -1)]
    for directions in directionsPairs:
        horDirection, verDirection = directions
        diagonalPositions = []
        startPosition = posLabel
        for x in range(8):
            print('startPosition', startPosition)
            forwardPos = getFowardPosition(startPosition, 1, verDirection)

            if not len(forwardPos):
                break

            newPosition = getSidewaysPosition(forwardPos[0], 1, horDirection)
            
            if not len(newPosition):
                break
            
            startPosition = newPosition[0]
            diagonalPositions.append(startPosition)
        
        possiblePositions.extend(diagonalPositions)

    
    return possiblePositions