from constants import removeInvalidPositionsByPieceOnTheWay, PlayerColor, getNumberPositionByLetter, getWorldPositionFromBoardPosition, getPygameColorByColor, SQUARE_SIZE, WIDTH, HEIGHT
from boardPosition import BoardPosition
from pieces.pieceFactory import PieceFactory 
from math import floor


class Board():
    currentPlayer = PlayerColor.white
    boards = []
    pieces = {
        PlayerColor.black: [],
        PlayerColor.white: [],
    }
    

    def __init__(self, startPositions=None):
        self.initBoard(startPositions)

    def getDefaultGameStartPositions(self):
        return [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

    def initBoard(self, startPositions = None):
        if not startPositions:
            startPositions = self.getDefaultGameStartPositions()

        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        for rowIdx, row in enumerate(startPositions):
            for columnIdx, column in enumerate(row):   
                currentColumn = columns[columnIdx]  
                posLabel = f'{column}{currentColumn}{8 - rowIdx}'
                piece = PieceFactory.buildByPositionLabel(posLabel)  
                board = BoardPosition(posLabel)  
                if(piece):
                    board.attachPiece(piece)
                
                self.addBoardData(board)

    def addBoardData(self, board):
        self.boards.append(board)
        piece = board.getPiece()
        if piece:
            if piece.color == PlayerColor.white:
                self.pieces[PlayerColor.white].append(piece)
            else: 
                self.pieces[PlayerColor.black].append(piece)

    def getAllPieces(self):
        return self.getWhitePieces() + self.getBlackPieces()

    def getWhitePieces(self):
        return self.pieces[PlayerColor.white]
    
    def getBlackPieces(self):
        return self.pieces[PlayerColor.black]

    def getBoards(self):
        return self.boards  

    def getBoardByWorldPos(self, worldPos):
        # todo: se colocar borda, arrumar aqui
        hor = worldPos[0] if worldPos[0] < WIDTH else WIDTH - 1 
        ver = worldPos[1] if worldPos[1] < HEIGHT else HEIGHT  - 1
        horSquareNumber = (floor(hor/ SQUARE_SIZE)) 
        verSquareNumber = floor(ver/ SQUARE_SIZE ) * 8
        board = self.boards[horSquareNumber + verSquareNumber]
        return board

    def drawBoards(self, pygame, display):
        for board in self.boards:
            hor, ver = getWorldPositionFromBoardPosition(board.getPositionLabel())
            color = getPygameColorByColor(board.color)
            pygame.draw.rect(display, color, pygame.Rect(hor, ver, SQUARE_SIZE, SQUARE_SIZE))

    def getBoardByPositionLabel(self, pos):
        horizontal = 9 - getNumberPositionByLetter(pos[0])
        vertical = (9 - int(pos[1])) * 8
        return self.boards[vertical - horizontal]
    
    def setAttackedPositions(self):
        self._clearBoardPositionsStatus()
        for board in self.boards:
            attackingPiece = board.getPiece() 
            if attackingPiece is None:
                continue
        
            self._checkBoardPositionsBeenAttacked(attackingPiece)
            self._checkKingBeenAttack(attackingPiece )

                

    def _clearBoardPositionsStatus(self):
        for board in self.boards:
            board.clearAttackedByPlayer()
            p = board.getPiece()
            if p:
                p.clearOnXRay()
    
    def _checkBoardPositionsBeenAttacked(self, attackingPiece):
        attackedPositions = removeInvalidPositionsByPieceOnTheWay(self, attackingPiece, attackingPiece.getAttackMoves())
        for labelPos in attackedPositions:
            boardBeenAttacked = self.getBoardByPositionLabel(labelPos)
            boardBeenAttacked.addToAttackedByPlayer(attackingPiece.getColor())

    def _checkKingBeenAttack(self, attackingPiece):
        attackedPositions = attackingPiece.getAttackMoves()
        firstPieceBeenAttacked = None
        secondPieceBeenAttacked = None
        for labelPos in attackedPositions:
             
            boardBeenAttacked = self.getBoardByPositionLabel(labelPos)
            pieceBeenAttacked = boardBeenAttacked.getPiece()
            if self._shouldCheckKingBeenAttacked(attackingPiece, pieceBeenAttacked):
                if firstPieceBeenAttacked is None:
                    
                    firstPieceBeenAttacked = pieceBeenAttacked
                    if firstPieceBeenAttacked.__class__.__name__ == "King":
                        self._verifyCheck()
                        self._verifyCheckmate()
                        break

                elif secondPieceBeenAttacked is None:
                    secondPieceBeenAttacked  = pieceBeenAttacked
                    if secondPieceBeenAttacked.__class__.__name__ == "King":
                        firstPieceBeenAttacked.addToOnXRay(attackingPiece.getBoardPosition())
                    
                    break

    def _shouldCheckKingBeenAttacked(self, attackingPiece, pieceBeenAttacked):
        if attackingPiece is None or pieceBeenAttacked is None:
            return False

        attackingPieceColor = attackingPiece.getColor()
        pieceBeenAttackedColor = pieceBeenAttacked.getColor()
        return attackingPieceColor != pieceBeenAttackedColor

    def _verifyCheck(self):
        pass

    def _verifyCheckmate(self):
        pass

#
#- pega primeira peça atacada 
#- se a proxima for o rei, ela está bloqueada