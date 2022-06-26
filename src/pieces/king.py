from pieces.piece import Piece
from constants import getAllDiagonalPositions, getAllHorizontalAndVerticalPositions

class King(Piece): 

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        diagonalPositions = getAllDiagonalPositions(posLabel, 1)
        ortogonalPositions = getAllHorizontalAndVerticalPositions(posLabel, 1)
        return diagonalPositions + ortogonalPositions
    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        pass