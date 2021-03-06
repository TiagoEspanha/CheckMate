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
    green = 6

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

def _getDirectionFromTwoPositions(pos1, pos2):
    pos1Letter = pos1[0]
    pos2Letter = pos2[0]
    pos1Number = pos1[1]
    pos2Number = pos2[1]
    
    isHorizontal = pos1Letter != pos2Letter
    isVertical = pos1Number != pos2Number

    isGoingUp = pos1Number < pos2Number 
    isGoingRight = getNumberPositionByLetter(pos1Letter) < getNumberPositionByLetter(pos2Letter)
    # so horizontal
    if isHorizontal and not isVertical:
        return Directions.right if isGoingRight else Directions.left
    elif isVertical and not isHorizontal:
        return Directions.top if isGoingUp else Directions.down
    else:
        if isGoingUp and isGoingRight:
            return Directions.topRight
        if isGoingUp and not isGoingRight:
            return Directions.topLeft
        if not isGoingUp and isGoingRight:
            return Directions.downRight
        if not isGoingUp and not isGoingRight:
            return Directions.downLeft

    # diagonal
    # se mudar so letra horizontal
    # se mudar so o numero vertical
    # se mudar os dois

def breakPositionsIntoDirection(piecePos, positions):
    breakPositions = {
        Directions.top: [],
        Directions.topRight: [],
        Directions.right: [],
        Directions.downRight: [],
        Directions.down: [],
        Directions.downLeft: [],
        Directions.left: [],
        Directions.topLeft: [],
    }

    for p in positions:        
        currentDirection = _getDirectionFromTwoPositions(piecePos, p)
        breakPositions[currentDirection].append(p)

    print('breakPositions', breakPositions)
    return breakPositions

def removeInvalidPositionsByPieceOnTheWay(board, piece, positions):
    if piece.__class__.__name__ == 'Knight':
        return positions

    labelPos = piece.getBoardPosition()

    directionsToCheck = [
        getForwardPosition(labelPos, direction=1),
        getForwardPosition(labelPos, direction=-1),
        getSidewaysPosition(labelPos, direction=1),
        getSidewaysPosition(labelPos, direction=-1),
        getDiagonalPositions(labelPos, direction=(1,1)),
        getDiagonalPositions(labelPos, direction=(1, -1)),
        getDiagonalPositions(labelPos, direction=(-1, 1)),
        getDiagonalPositions(labelPos, direction=(-1, -1)),
    ]

    bannedPositions = set()
    for direction in directionsToCheck:
        pieceWasFound = False
        for position in direction:
            if pieceWasFound:
                bannedPositions.add(position)    
                continue

            boardPos = board.getBoardByPositionLabel(position)
            piece = boardPos.getPiece()
            if piece is not None:
                pieceWasFound = True
                                               
    
    validPositions = [p for p in positions if p not in bannedPositions]
    return validPositions


def _calculateAmountOfBoardPositionsBetweenPositions(pos1, pos2):
    pos1Letter = pos1[0]
    pos2Letter = pos2[0]
    pos1Number = pos1[1]
    pos2Number = pos2[1]

    if pos1Number == pos2Number:
        return abs(getNumberPositionByLetter(pos1Letter) - getNumberPositionByLetter(pos2Letter))

    return abs(int(pos1Number) - int(pos2Number))

    


#todo: tem posicoes q nao tem como tracar uma linha
def getPositionsOnLineBetweenPos(pos1, pos2):
    direction = _getDirectionFromTwoPositions(pos1, pos2)
    amount = _calculateAmountOfBoardPositionsBetweenPositions(pos1, pos2)
    
    if direction == Directions.top:
        return getForwardPosition(pos1, amount, 1)


    if direction == Directions.right:
        return getSidewaysPosition(pos1, amount, 1)

    if direction == Directions.down:
        return getForwardPosition(pos1, amount, -1)

    if direction == Directions.left:
        return getSidewaysPosition(pos1, amount, -1)
        
    return getDiagonalPositions(pos1, amount, direction.value)
