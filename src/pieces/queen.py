from pieces.piece import Piece
from constants import getAllDiagonalPositions, getAllHorizontalAndVerticalPositions

class Queen(Piece): 

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        diagonalPositions = getAllDiagonalPositions(posLabel)
        ortogonalPositions = getAllHorizontalAndVerticalPositions(posLabel)
        return diagonalPositions + ortogonalPositions
    
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