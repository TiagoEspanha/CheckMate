from pieces.piece import Piece
from constants import getFowardPosition, getBoardPositionFromWorldPosition, getSidewaysPosition

class Pawn(Piece): 
    firstMove = True

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        direction = 1 if self.isWhite() else -1

        if(self.firstMove):
            return getFowardPosition(posLabel, 2, direction)
            
        return getFowardPosition(posLabel, 1, direction)
    
    def getAttackMoves(self):
        possibleMoves = []
        posLabel = self.getBoardPosition()
        direction = 1
        
        forwardPos = getFowardPosition(posLabel, 1, direction)
        atkOne = getSidewaysPosition(forwardPos[0], 1, direction * -1)
        atkTwo = getSidewaysPosition(forwardPos[0], 1, direction) 
        
        if len(atkOne):
            possibleMoves.append(atkOne[0])

        if len(atkTwo):
            possibleMoves.append(atkTwo[0])

        return possibleMoves
    
    def move(self):
        pass
    
        
    def posMove(self):
        self.firstMove = False

    def attack():
        pass