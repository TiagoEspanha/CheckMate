from constants import PlayerColor, BoardPositionColor, SQUARE_SIZE, LETTER_POS_LABEL, getWorldPositionFromBoardPosition
from pieces.pawn import Pawn
from pieces.tower import Tower
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King

class BoardPosition(): 
    position = None
    color = None
    piece = None 


    def __init__(self, setup):
        self.setPosition(setup) 
        self.setPiece(setup)        


    def setPiece(self, setup):
        pieceColor = self.getPieceColorByLabel(setup[0])
        pieceClass = self.getPieceByLabel(setup[1])
        
        if(pieceClass):
            self.piece = pieceClass(pieceColor, self.getPieceWorldPosition())

    def setPosition(self, setup):
        pos = setup[2:]
        self.position = pos
        self.color = self.getPositionColorByLabel(pos)

    def getPieceByLabel(self, label):
        pieceByLabel = {
            'P': Pawn,
            'R': Tower,
            'B': Bishop,
            'N': Knight,
            'Q': Queen,
            'K': King,
            '-': None,
        }
        return pieceByLabel[label]

    def getPieceColorByLabel(self, label):
        pieceColorByLabel = {
            'b': PlayerColor.black,
            'w': PlayerColor.white,
            '-': None
        }
        return pieceColorByLabel[label]

    def getPositionColorByLabel(self, label):
        letterPos = label[0]
        numberPos = int(label[1])
        return BoardPositionColor.white if (LETTER_POS_LABEL[letterPos] + numberPos) % 2 else BoardPositionColor.black
        
        
    def getPiece(self):
        return self.piece

    def getPieceWorldPosition(self):
        hor, ver = getWorldPositionFromBoardPosition(self.position)
        return (hor + SQUARE_SIZE/2, ver + SQUARE_SIZE/2)