from pieces.piece import Piece
from constants import getAllHorizontalAndVerticalPositions

class Tower(Piece): 

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        return getAllHorizontalAndVerticalPositions(posLabel)
    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        pass