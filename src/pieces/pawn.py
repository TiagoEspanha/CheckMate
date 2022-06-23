from pieces.piece import Piece
from constants import getFowardPosition, getBoardPositionFromWorldPosition

class Pawn(Piece): 
    firstMove = True

    def getPossibleMoves(self):
        posLabel = self.getBoardPosition()
        
        if(self.firstMove):
            return getFowardPosition(posLabel, 2)
            
        return getFowardPosition(posLabel, 1)
    
    
    def move(self):
        pass
    
        
    def posMove(self):
        self.firstMove = False

    def attack():
        pass