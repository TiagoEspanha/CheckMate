from constants import BoardPositionColor, SQUARE_SIZE, LETTER_POS_LABEL, getWorldPositionFromBoardPosition


class BoardPosition(): 
    positionLabel = None
    color = None
    piece = None 
    attackedByPlayer = set()


    def __init__(self, setup):
        self.setPosition(setup) 

    def setPosition(self, setup):
        pos = setup[2:]
        self.positionLabel = pos
        self._setPositionColorByLabel()

    def attachPiece(self, piece):
        self.piece = piece 
        piece.setWorldPosition(self.getPieceWorldPosition())

    def detachPiece(self):
        p = self.piece 
        self.piece = None
        return p

    def getPiece(self):
        return self.piece

    def getPieceColor(self):
        if self.piece:
            return self.piece.getColor()

    def getPieceWorldPosition(self):
        hor, ver = getWorldPositionFromBoardPosition(self.positionLabel)
        return (hor + SQUARE_SIZE/2, ver + SQUARE_SIZE/2)

    def getPositionLabel(self):
        return self.positionLabel

    def addToAttackedByPlayer(self, color):
        self.attackedByPlayer.add(color)
        self._setColor(BoardPositionColor.red)

    def removeFromAttackedByPlayer(self, color):
        self.attackedByPlayer.remove(color)
        
    def clearAttackedByPlayer(self):
        self.attackedByPlayer.clear()
        self._setPositionColorByLabel()

    def _setColor(self, color):
        self.color = color

    def _setPositionColorByLabel(self):
        letterPos = self.positionLabel[0]
        numberPos = int(self.positionLabel[1])
        self.color = BoardPositionColor.white if (LETTER_POS_LABEL[letterPos] + numberPos) % 2 else BoardPositionColor.black
