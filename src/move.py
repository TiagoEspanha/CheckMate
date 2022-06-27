from enum import Enum

class MoveStates(Enum):
    choosingPiece = 1
    choosingMove = 2
    validatingMove = 3
    executingMovementMove = 4
    executingAttackMove = 5
    rollingBackMove = 6
    done = 7

class Move():
    startBoardPosition = None
    endBoardPosition = None 
    piece = None
    movementMoves = None
    attackMoves = None
    currentState = MoveStates.choosingPiece

    def setInitialState(self, piece, boardPosition):
        self.startBoardPosition = boardPosition
        self.piece = piece
        self.movementMoves = piece.getMovementMoves()
        self.attackMoves = piece.getAttackMoves()
        piece.getAttackMoves()
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
        if self.endBoardPosition.getPositionLabel() in self.movementMoves and self.endBoardPosition.getPiece() is None:
            self.executeMovementMove()
        elif self.endBoardPosition.getPositionLabel() in self.attackMoves and self.endBoardPosition.getPiece() is not None:
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

    def rollbackMove(self):
        self._changeState(MoveStates.rollingBackMove)
        self.startBoardPosition.attachPiece(self.piece)
        self._changeState(MoveStates.choosingPiece)

    def finishMove(self):
        self._changeState(MoveStates.done)

    def _changeState(self, state):
        print(f'from {self.currentState.name} to {state.name}')
        self.currentState = state

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
