import pygame
from abc import ABC, abstractmethod

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

    def getImage(self):
        piece = self.__class__.__name__.lower()
        return f'sprites/{piece}_{self.color.name}.png'

    def update(self):
        self.handleMove()

    def handleMove(self):
        if self.state == 'selected': 
           self.rect.center = pygame.mouse.get_pos()

    def handleSelect(self, pos):
        if self.rect.collidepoint(pos) and self.state == 'free': 
            print(f'{self.__class__.__name__} selected!')
            self.state = 'selected'
            return self.preMove()

    def handleDrop(self, pos, boardToMove):
        if self.rect.collidepoint(pos) and self.state == 'selected': 
            self.state = 'free'
            self.posMove(boardToMove)

    @abstractmethod
    def preMove(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def posMove(self):
        pass 

    @abstractmethod
    def attack(self):
        pass

