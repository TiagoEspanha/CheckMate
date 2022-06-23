import pygame 
from move import Move
from board import Board
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP 
from sys import exit


pygame.init()

config = {
    'name': "CheckMate",
    'width': 800,
    'heigh': 800
}

game_states = [
    'choosing_a_piece', # espera o jogador escolher qual peça (botao do mouse ser clicado)
    'choosing_a_move',  # espera o jogador escolher qual movimento (botao do mouse ser solto)
    'validating_move',  # valida 
    'evaluating_move'
]

display = pygame.display.set_mode((config['width'], config['heigh']))
pygame.display.set_caption(config['name'])

board = Board()
pieces = board.getAllPieces()
boardsGroup = pygame.sprite.Group()
boardsGroup.add(board.getAllPieces())
moves = []
currentMove = None

while True:
    if not currentMove:
        currentMove = Move()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # abstrair movimeto inteiro?
        if event.type == MOUSEBUTTONDOWN:
            clickedBoard = board.getBoardByWorldPos(event.pos)
            piece = clickedBoard.getPiece()
            if(piece):
                currentMove.setInitialState(piece, clickedBoard)

        if event.type == MOUSEBUTTONUP:
            boardToMove = board.getBoardByWorldPos(event.pos)
            currentMove.setMove(boardToMove)

    display.fill((255, 255, 0))
    board.drawBoards(pygame, display)
    boardsGroup.update()
    boardsGroup.draw(display)
    
    pygame.display.update() 
    


    
        