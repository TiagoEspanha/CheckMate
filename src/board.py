from constants import PlayerColor, getNumberPositionByLetter, getWorldPositionFromBoardPosition, getPygameColorByColor, SQUARE_SIZE
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
                print(posLabel)
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
        hor = (floor(worldPos[0]/ SQUARE_SIZE) - 1) 
        ver = floor(worldPos[1]/ SQUARE_SIZE ) * 8
        board = self.boards[hor + ver]
        return board


    def drawBoards(self, pygame, display):
        for board in self.boards:
            hor, ver = getWorldPositionFromBoardPosition(board.getPositionLabel())
            color = getPygameColorByColor(board.color)
            pygame.draw.rect(display, color, pygame.Rect(hor, ver, SQUARE_SIZE, SQUARE_SIZE))

    def drawPieces(self, pygame, display):
        pass

    def getBoardByPositionLabel(self, pos):
        return self.boards[(getNumberPositionByLetter(pos[0]) - 1) * 8 + int(pos[1]) - 1]
        


    