from turtle import right
from pygame import Color
from math import floor
from enum import Enum

class PlayerColor(Enum):
    white = 1
    black = 2

class BoardPositionColor(Enum):
    white = 1
    black = 2
    red = 3
    orange = 4
    yellow = 5

class Directions(Enum):
    top = (0, 1)
    topRight = (1, 1)
    right = (1, 0)
    downRight = (1,-1)
    down  = (0, -1)
    downLeft = (-1, -1)
    left = (-1, 0)
    topLeft = (-1, 1)

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
    horizontalPos = (getNumberPositionByLetter(boardPos[0]) - 1) * SQUARE_SIZE
    verticalPos = (8 - int(boardPos[1])) * SQUARE_SIZE
    return (horizontalPos, verticalPos)

def getBoardPositionFromWorldPosition(worldPos):
    letter = getLetterByNumberPosition(floor(worldPos[0]/ SQUARE_SIZE) + 1)
    num = 8 - floor(worldPos[1]/ SQUARE_SIZE )
    return f'{letter}{num}'

def getPygameColorByColor(color):
    if(color.name == 'black'):
        return Color('grey')
    
    return Color(color.name)


def getForwardPosition(posLabel, amount=8, direction=1):
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

def getDiagonalPositions(posLabel, amount=8, direction=(1,1)):
    possiblePositions = []
    horDirection, verDirection = direction
    startPosition = posLabel
    for x in range(amount):
        forwardPos = getForwardPosition(startPosition, 1, verDirection)

        if not len(forwardPos):
            break

        newPosition = getSidewaysPosition(forwardPos[0], 1, horDirection)
        
        if not len(newPosition):
            break
        
        startPosition = newPosition[0]
        possiblePositions.append(startPosition)
    return possiblePositions

def getAllHorizontalAndVerticalPositions(posLabel, amount=8):
    possiblePositions = []
    leftPos = getSidewaysPosition(posLabel, amount, 1)
    rightPos = getSidewaysPosition(posLabel, amount, -1)
    forwardPos = getForwardPosition(posLabel, amount, 1)
    backwardPos = getForwardPosition(posLabel, amount, -1)
    
    possiblePositions.extend(leftPos)
    possiblePositions.extend(rightPos)
    possiblePositions.extend(forwardPos)
    possiblePositions.extend(backwardPos)

    return possiblePositions

def getAllDiagonalPositions(posLabel, amount=8):
    possiblePositions = []
    directionsPairs = [(1,1), (1, -1), (-1, 1), (-1, -1)]
    for directions in directionsPairs:
        horDirection, verDirection = directions
        diagonalPositions = []
        startPosition = posLabel
        for x in range(amount):
            forwardPos = getForwardPosition(startPosition, 1, verDirection)

            if not len(forwardPos):
                break

            newPosition = getSidewaysPosition(forwardPos[0], 1, horDirection)
            
            if not len(newPosition):
                break
            
            startPosition = newPosition[0]
            diagonalPositions.append(startPosition)
        
        possiblePositions.extend(diagonalPositions)

    
    return possiblePositions