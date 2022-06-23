import pygame
from abc import ABC, abstractmethod
from constants import getBoardPositionFromWorldPosition

class Piece(ABC, pygame.sprite.Sprite):

    states = ['free', 'selected']
    state = 'free'
    color = None
    
    def __init__(self, color=None):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.image.load(self.getImage())
        self.rect = self.image.get_rect()
    
    def setWorldPosition(self, pos):
        self.rect.center = pos

    def getWorldPosition(self):
        return self.rect.center

    def getBoardPosition(self):
        return getBoardPositionFromWorldPosition(self.getWorldPosition())

    def getImage(self):
        piece = self.__class__.__name__.lower()
        return f'sprites/{piece}_{self.color.name}.png'

    def update(self):
        self.handleMove()

    def handleMove(self):
        if self.state == 'selected': 
            self.rect.center = pygame.mouse.get_pos()

    def handleSelect(self):
        if self.state == 'free': 
            print(f'{self.__class__.__name__} selected!')
            self.state = 'selected'
            return self

    def handleDrop(self):
        if self.state == 'selected': 
            print(f'{self.__class__.__name__} deselected!')
            self.state = 'free'
            


    @abstractmethod
    def getPossibleMoves(self):
        pass
    

    @abstractmethod
    def posMove(self):
        pass 

    @abstractmethod
    def attack(self):
        pass
