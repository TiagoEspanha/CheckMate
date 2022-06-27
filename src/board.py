from constants import PlayerColor, BoardPositionColor, getWorldPositionFromBoardPosition, getPygameColorByColor, SQUARE_SIZE
from pieces.pawn import Pawn
from pieces.tower import Tower
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King
from boardPosition import BoardPosition


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

        for columnIdx, column in enumerate(startPositions):
            currentColumn = columns[columnIdx]
            for rowId, row in enumerate(column):      
                print(f'{row}{currentColumn}{8 - rowId}')
                board = BoardPosition(f'{row}{currentColumn}{8 - rowId}')          
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

    def drawBoards(self, pygame, display):
        for board in self.boards:
            hor, ver = getWorldPositionFromBoardPosition(board.position)
            color = getPygameColorByColor(board.color)
            pygame.draw.rect(display, color, pygame.Rect(hor, ver, SQUARE_SIZE, SQUARE_SIZE))

    def drawPieces(self, pygame, display):
        pass


    