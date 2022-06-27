from pieces.piece import Piece
from constants import getAllHorizontalAndVerticalPositions

class Tower(Piece): 
    firstMove = True

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        return getAllHorizontalAndVerticalPositions(posLabel)
    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        self.firstMove = False

    def getSpecialMoves(self):
        return []

    
    def executeSpecialMove(self, board):
        pass

    
    def validateSpecialMove(self, board):
        return True