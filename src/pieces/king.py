from pieces.piece import Piece
from constants import getAllDiagonalPositions, getAllHorizontalAndVerticalPositions, getPositionsOnLineBetweenPos

class King(Piece): 
    firstMove = True
    isChecked = False
    isDoubleChecked = False
    piecesChecking = []

    def getMovementMoves(self):
        posLabel = self.getBoardPosition()
        diagonalPositions = getAllDiagonalPositions(posLabel, 1)
        ortogonalPositions = getAllHorizontalAndVerticalPositions(posLabel, 1)
        return diagonalPositions + ortogonalPositions
    
    def getAttackMoves(self):
        return self.getMovementMoves()
        
    def posMove(self):
        self.firstMove = False

    def getSpecialMoves(self):
        if not self.firstMove:
            return []

        if self.isWhite():
            return ['c1', 'g1']

        return ['c8', 'g8']

    def executeSpecialMove(self, board):
        towerStartBoardPos, towerEndBoardPos, kingStartBoardPos, kingEndBoardPos = self._getCastlingBoardData(board)
        tower = towerStartBoardPos.getPiece()

        kingStartBoardPos.detachPiece()
        kingEndBoardPos.attachPiece(self)
        
        towerStartBoardPos.detachPiece()
        towerEndBoardPos.attachPiece(tower)

        self.posMove()
        tower.posMove()
        
    
    def validateSpecialMove(self, board):
        towerStartBoardPos, towerEndBoardPos, _, _ = self._getCastlingBoardData(board)
        tower = towerStartBoardPos.getPiece()
        return tower and tower.firstMove and towerEndBoardPos.getPiece() == None

    def _getCastlingBoardData(self, board):
        kingPos = self.getBoardPosition()
        towerPosByKingPos = {
            'c1': {
                'startPos': 'a1', 
                'finalPos': 'd1',
            },
            'g1': {
                'startPos': 'h1', 
                'finalPos': 'f1',
            },
            'c8': {
                'startPos': 'a8', 
                'finalPos': 'd8',
            }, 
            'g8': {
                'startPos': 'h8', 
                'finalPos': 'f8',
            },
        }

        towerData = towerPosByKingPos[kingPos]

        towerStartBoardPos = board.getBoardByPositionLabel(towerData['startPos'])
        towerEndBoardPos = board.getBoardByPositionLabel(towerData['finalPos'])
        kingStartBoardPos = board.getBoardByPositionLabel('e1' if self.isWhite() else 'e8')
        kingEndBoardPos = board.getBoardByPositionLabel(self.getBoardPosition())
        return towerStartBoardPos, towerEndBoardPos, kingStartBoardPos, kingEndBoardPos

    def setCheck(self, pieceChecking):
        if self.isChecked:
            self.isDoubleChecked = True
        
        self.isChecked = True
        self.piecesChecking.append(pieceChecking)

    def removeCheck(self):
        self.isDoubleChecked = False
        self.isChecked = False
        self.piecesChecking = []

    def getPiecesChecking(self):
        return self.piecesChecking

    def isOnCheck(self):
        return self.isChecked

    def isOnDoubleCheck(self):
        return self.isDoubleChecked

    def getValidMovesIfChecked(self):
        return getPositionsOnLineBetweenPos(self.getBoardPosition(), self.getPiecesChecking()[0].getBoardPosition()) 

        