import pygame 
from board import Board
from gameManager import GameManager
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP 
from sys import exit


pygame.init()

config = {
    'name': "CheckMate",
    'width': 800,
    'heigh': 800
}

display = pygame.display.set_mode((config['width'], config['heigh']))
pygame.display.set_caption(config['name'])

board = Board()
pieces = board.getAllPieces()
boardsGroup = pygame.sprite.Group()
boardsGroup.add(board.getAllPieces())
gameManager = GameManager(board)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # abstrair movimeto inteiro?
        if event.type == MOUSEBUTTONDOWN:
            gameManager.executeRoundStart(event.pos)

        if event.type == MOUSEBUTTONUP:
            gameManager.executeRoundEnd(event.pos)
            

    display.fill((255, 255, 0))
    board.drawBoards(pygame, display)
    boardsGroup.update()
    boardsGroup.draw(display)
    
    pygame.display.update() 
    


    
        