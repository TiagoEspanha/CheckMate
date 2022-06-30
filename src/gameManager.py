from constants import PlayerColor
from move import Move

class GameManager():
    players = [PlayerColor.white, PlayerColor.black]
    currentPlayer = 0
    moves = []
    currentMove = None
    board = None

    def __init__(self, board):
        self.board = board
        self.currentMove = Move(board) 

    def executeRoundStart(self, mouseClickPos):
        clickedBoard = self.board.getBoardByWorldPos(mouseClickPos)
        piece = clickedBoard.getPiece()
        if(piece and piece.getColor() == self._getCurrentPlayer()):
            self.currentMove.setInitialState(piece, clickedBoard)

    def executeRoundEnd(self, mouseClickPos):
        boardToMove = self.board.getBoardByWorldPos(mouseClickPos)
        self.currentMove.setMove(boardToMove)
        if self.currentMove.isDone(): 
            self._finishTurn()    
       
    def _changeCurrentPlayer(self):
        self.currentPlayer += 1
        if self.currentPlayer >= len(self.players):
            self.currentPlayer = 0

    def _getCurrentPlayer(self):
        return self.players[self.currentPlayer]

    def _finishTurn(self):
        self.moves.append(self.currentMove)
        self.currentMove = Move(self.board) 
        self._changeCurrentPlayer()
        self.board.setAttackedPositions()