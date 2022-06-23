from constants import BoardPositionColor, SQUARE_SIZE, LETTER_POS_LABEL, getWorldPositionFromBoardPosition


class BoardPosition(): 
    positionLabel = None
    color = None
    piece = None 


    def __init__(self, setup):
        self.setPosition(setup) 

    def setPosition(self, setup):
        pos = setup[2:]
        self.positionLabel = pos
        self.color = self.getPositionColorByLabel(pos)

    def attachPiece(self, piece):
        self.piece = piece 
        piece.setWorldPosition(self.getPieceWorldPosition())

    def detachPiece(self):
        self.piece = None

    def getPositionColorByLabel(self, label):
        letterPos = label[0]
        numberPos = int(label[1])
        return BoardPositionColor.white if (LETTER_POS_LABEL[letterPos] + numberPos) % 2 else BoardPositionColor.black
        
    def getPiece(self):
        return self.piece

    def getPieceWorldPosition(self):
        hor, ver = getWorldPositionFromBoardPosition(self.positionLabel)
        return (hor + SQUARE_SIZE/2, ver + SQUARE_SIZE/2)

    def getPositionLabel(self):
        return self.positionLabel