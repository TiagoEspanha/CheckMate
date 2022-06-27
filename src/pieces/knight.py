from turtle import back, pos
from pieces.piece import Piece
from constants import getForwardPosition, getSidewaysPosition

class Knight(Piece): 
    
    def getMovementMoves(self):
        possiblePositions = []
        posLabel = self.getBoardPosition()
        
        forwardPos = getForwardPosition(posLabel, 2, 1)
        if len(forwardPos) == 2:            
            possiblePositions.extend(getSidewaysPosition(forwardPos[1], 1, 1))
            possiblePositions.extend(getSidewaysPosition(forwardPos[1], 1, -1))

        backPos = getForwardPosition(posLabel, 2, -1)
        if len(backPos) == 2:
            possiblePositions.extend(getSidewaysPosition(backPos[1], 1, 1))
            possiblePositions.extend(getSidewaysPosition(backPos[1], 1, -1))

        leftPos = getSidewaysPosition(posLabel, 2, 1)
        if len(leftPos) == 2:
            possiblePositions.extend(getForwardPosition(leftPos[1], 1, 1))
            possiblePositions.extend(getForwardPosition(leftPos[1], 1, -1))

        rightPos = getSidewaysPosition(posLabel, 2, -1)
        if len(rightPos) == 2:
            possiblePositions.extend(getForwardPosition(rightPos[1], 1, 1))
            possiblePositions.extend(getForwardPosition(rightPos[1], 1, -1))

        return possiblePositions

    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        pass

    def getSpecialMoves(self):
        return []

    
    def executeSpecialMove(self, board):
        pass

    
    def validateSpecialMove(self, board):
        return True