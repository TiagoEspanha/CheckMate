from enum import Enum

class MoveStates(Enum):
    choosingPiece = 1
    choosingMove = 2
    validatingMove = 3
    executingMovementMove = 4
    executingAttackMove = 5
    executingSpecialMove = 6
    rollingBackMove = 7
    done = 8

class Move():
    board = None
    startBoardPosition = None
    endBoardPosition = None 
    piece = None
    movementMoves = None
    attackMoves = None
    specialMoves = None
    currentState = MoveStates.choosingPiece

    def __init__(self, board):
        self.board = board

    def setInitialState(self, piece, boardPosition):
        self.startBoardPosition = boardPosition
        self.piece = piece
        self.movementMoves = piece.getMovementMoves()
        self.attackMoves = piece.getAttackMoves()
        self.specialMoves = piece.getSpecialMoves()
        self.piece.handleSelect()
        self._changeState(MoveStates.choosingMove)

    def setMove(self, boardPosition):
        if not self.currentState == MoveStates.choosingMove:
            return
        
        self.endBoardPosition = boardPosition
        self.piece.handleDrop()
        self.validateMove()

    def validateMove(self):
        self._changeState(MoveStates.validatingMove)
        if self._validateSpecialMove():
            self.executeSpecialMove()
        elif self._validateMovementMove():
            self.executeMovementMove()
        elif self._validateAttackMove():
            self.executeAttackMove()
        else:
            self.rollbackMove()
    
    def executeAttackMove(self):
        self._changeState(MoveStates.executingAttackMove)
        self.startBoardPosition.detachPiece()
        otherPiece = self.endBoardPosition.detachPiece()
        otherPiece.destroy()
        self.endBoardPosition.attachPiece(self.piece)
        self.piece.posMove()
        self.finishMove()

    def executeMovementMove(self):
        self._changeState(MoveStates.executingMovementMove)
        self.startBoardPosition.detachPiece()
        self.endBoardPosition.attachPiece(self.piece)
        self.piece.posMove()
        self.finishMove()

    def executeSpecialMove(self):
        self._changeState(MoveStates.executingSpecialMove)
        self.piece.executeSpecialMove(self.board)
        self.finishMove()

    def rollbackMove(self):
        self._changeState(MoveStates.rollingBackMove)
        self.startBoardPosition.attachPiece(self.piece)
        self._changeState(MoveStates.choosingPiece)

    def finishMove(self):
        self._changeState(MoveStates.done)

    def _changeState(self, state):
        print(f'from {self.currentState.name} to {state.name}')
        self.currentState = state

    def _validateMovementMove(self):
        isOnMovementMoves = self.endBoardPosition.getPositionLabel() in self.movementMoves
        boardPosIsFree = self.endBoardPosition.getPiece() is None
        return isOnMovementMoves and boardPosIsFree
        
    def _validateAttackMove(self):
        pieceOnAttackPos = self.endBoardPosition.getPiece()
        if not pieceOnAttackPos:
            return False 
        
        isValidAttackPos = self.endBoardPosition.getPositionLabel() in self.attackMoves
        pieceMoving = self.startBoardPosition.getPiece()
        pieceIsEnemy = pieceOnAttackPos.isWhite() != pieceMoving.isWhite()

        return isValidAttackPos and pieceIsEnemy

    def _validateSpecialMove(self):
        isOnSpecialPosition = self.endBoardPosition.getPositionLabel() in self.specialMoves
        return isOnSpecialPosition and self.piece.validateSpecialMove(self.board)

    def print(self):
        piece = f'piece: {self.piece.__class__.__name__}' if self.piece else 'piece: none'
        startBoardPosition = f'startBoardPosition: {self.startBoardPosition}' 
        endBoardPosition = f'endBoardPosition: {self.endBoardPosition}' 
        movementMoves = f'movementMoves: {self.movementMoves}'
        msg = '''
            {piece}
            {startBoardPosition}
            {endBoardPosition}
            {movementMoves}
        '''
        print(msg)
