from constants import PlayerColor,BoardPositionColor, SQUARE_SIZE, LETTER_POS_LABEL, getWorldPositionFromBoardPosition


class BoardPosition(): 
    positionLabel = None
    color = None
    piece = None 
    attackedByBlack = False
    attackedByWhite = False


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
        if color == PlayerColor.black:
            self.attackedByBlack = True
            self._setColor(BoardPositionColor.red)

        if color == PlayerColor.white:
            self.attackedByWhite = True
            self._setColor(BoardPositionColor.orange)

    def removeFromAttackedByPlayer(self, color):
        if color == PlayerColor.black:
            self.attackedByBlack = False
            self._setPositionColorByLabel()

        if color == PlayerColor.white:
            self.attackedByWhite = False
            self._setPositionColorByLabel()
        
    def clearAttackedByPlayer(self):
        self.removeFromAttackedByPlayer(PlayerColor.black)
        self.removeFromAttackedByPlayer(PlayerColor.white)

    def isBeenAttackedByColor(self, color):
        if color == PlayerColor.black:
            return self.attackedByBlack
        
        if color == PlayerColor.white:
            return self.attackedByWhite


    def _setColor(self, color):
        self.color = color

    def _setPositionColorByLabel(self):
        letterPos = self.positionLabel[0]
        numberPos = int(self.positionLabel[1])
        self.color = BoardPositionColor.white if (LETTER_POS_LABEL[letterPos] + numberPos) % 2 else BoardPositionColor.black
