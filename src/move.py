from enum import Enum
from constants import getForwardPosition,getSidewaysPosition, getDiagonalPositions
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
        self.movementMoves = self._getValidMovementMoves()
        self.attackMoves = self._getValidAttackMoves()
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

    def isDone(self):
        return self.currentState == MoveStates.done

    def _getValidMovementMoves(self):
        return self._removeInvalidPositions(self.piece.getMovementMoves())

    def _getValidAttackMoves(self):
        return self._removeInvalidPositions(self.piece.getAttackMoves())

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

    def _removeInvalidPositions(self, positions):
        positions1 = self._removeInvalidPositionsByXRay(positions)    
        positions2 = self._removeInvalidPositionsByPieceOnTheWay(positions1)
        return positions2

    def _removeInvalidPositionsByXRay(self, positions):
        if not self.piece.isOnXRay():
            return positions

        return [p for p in positions if p in self.piece.onXRay] 

    def _removeInvalidPositionsByPieceOnTheWay(self, positions):
        if self.piece.__class__ == 'Knight':
            return positions

        labelPos = self.piece.getBoardPosition()

        directionsToCheck = [
            getForwardPosition(labelPos, direction=1),
            getForwardPosition(labelPos, direction=-1),
            getSidewaysPosition(labelPos, direction=1),
            getSidewaysPosition(labelPos, direction=-1),
            getDiagonalPositions(labelPos, direction=(1,1)),
            getDiagonalPositions(labelPos, direction=(1, -1)),
            getDiagonalPositions(labelPos, direction=(-1, 1)),
            getDiagonalPositions(labelPos, direction=(-1, -1)),
        ]

        bannedPositions = set()
        for direction in directionsToCheck:
            pieceWasFound = False
            for position in direction:
                if pieceWasFound:
                    bannedPositions.add(position)    
                    continue

                boardPos = self.board.getBoardByPositionLabel(position)
                piece = boardPos.getPiece()
                if piece is not None:
                    pieceWasFound = True                               
        
        validPositions = [p for p in positions if p not in bannedPositions]
        return validPositions

        

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
