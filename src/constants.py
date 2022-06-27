from pygame import Color
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


def getWorldPositionFromBoardPosition(boardPos):
    verticalPos = LETTER_POS_LABEL[boardPos[0]] * SQUARE_SIZE
    horizontalPos = int(boardPos[1]) * SQUARE_SIZE
    return (horizontalPos, verticalPos)

def getPygameColorByColor(color):
    if(color.name == 'white'):
        return Color('white')

    if(color.name == 'black'):
        return Color('grey')