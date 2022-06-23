from pieces.piece import Piece
from constants import getFowardPosition, getBoardPositionFromWorldPosition

class Pawn(Piece): 
    firstMove = True

    def getPossibleMoves(self):
        posLabel = self.getBoardPosition()
        direction = 1 if self.isWhite() else -1

        if(self.firstMove):
            return getFowardPosition(posLabel, 2, direction)
            
        return getFowardPosition(posLabel, 1, direction)
    
    
    def move(self):
        pass
    
        
    def posMove(self):
        self.firstMove = False

    def attack():
        pass