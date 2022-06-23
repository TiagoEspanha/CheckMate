from enum import Enum

class MoveStates(Enum):
    choosingPiece = 1
    choosingMove = 2
    validatingMove = 3
    executingMove = 4
    rollingBackMove = 5
    done = 6

class Move():
    startBoardPosition = None
    endBoardPosition = None 
    piece = None
    possibleMoves = None

    def __init__(self):
        self.currentState = MoveStates.choosingPiece

    def setInitialState(self, piece, boardPosition):
        self.startBoardPosition = boardPosition
        self.piece = piece
        self.possibleMoves = piece.getPossibleMoves()
        self.piece.handleSelect()
        self._changeState(MoveStates.choosingMove)

    def setMove(self, boardPosition):
        self.endBoardPosition = boardPosition
        self.piece.handleDrop()
        self.validateMove()

    def validateMove(self):
        self._changeState(MoveStates.validatingMove)
        if(self.endBoardPosition.getPositionLabel() in self.possibleMoves):
            self.executeMove()
        else:
            self.rollbackMove()
    
    def executeMove(self):
        self._changeState(MoveStates.executingMove)
        self.startBoardPosition.detachPiece()
        self.endBoardPosition.attachPiece(self.piece)
        self.piece.posMove()

    def rollbackMove(self):
        self._changeState(MoveStates.rollingBackMove)
        self.startBoardPosition.attachPiece(self.piece)

    def finishMove(self):
        self._changeState(MoveStates.done)

    def _changeState(self, state):
        print(f'from {self.currentState.name} to {state.name}')
        self.currentState = state

    def print(self):
        piece = f'piece: {self.piece.__class__.__name__}' if self.piece else 'piece: none'
        startBoardPosition = f'startBoardPosition: {self.startBoardPosition}' 
        endBoardPosition = f'endBoardPosition: {self.endBoardPosition}' 
        possibleMoves = f'possibleMoves: {self.possibleMoves}'
        msg = '''
            {piece}
            {startBoardPosition}
            {endBoardPosition}
            {possibleMoves}
        '''
        print(msg)
