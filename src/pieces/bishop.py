from pieces.piece import Piece
from constants import getAllDiagonalPositions

class Bishop(Piece): 

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        return getAllDiagonalPositions(posLabel)
    
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

    