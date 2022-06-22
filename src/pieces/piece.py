import pygame
from abc import ABC, abstractmethod

class Piece(ABC, pygame.sprite.Sprite):

    states = ['free', 'selected']
    state = 'free'
    
    def __init__(self, color=None, startPosition=None):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.image.load(self.getImage())
        self.rect = self.image.get_rect()
        self.rect.center = startPosition
    
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
            print('selected!')
            self.state = 'selected'

    def handleDrop(self, pos):
        if self.rect.collidepoint(pos) and self.state == 'selected': 
            print('free!')
            self.state = 'free'

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def attack():
        pass
