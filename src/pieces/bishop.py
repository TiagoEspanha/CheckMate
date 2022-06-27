from pieces.piece import Piece
from constants import getDiagonalPosition

class Bishop(Piece): 

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        return getDiagonalPosition(posLabel)
    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        pass

    