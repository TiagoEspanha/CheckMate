import pygame
from abc import ABC, abstractmethod
from constants import PlayerColor, getBoardPositionFromWorldPosition, WIDTH, HEIGHT

class Piece(ABC, pygame.sprite.Sprite):

    states = ['free', 'selected']
    state = 'free'
    color = None
    onXRay = set()
    
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
        if  self.state == 'selected':
            mouseHorPos, mouseVerPos =  pygame.mouse.get_pos()
            isValidHorizontalPos = mouseHorPos <= WIDTH and mouseHorPos >= 0
            isValidVerticalPos = mouseVerPos <= HEIGHT and mouseVerPos >= 0
            newHorPos = mouseHorPos if isValidHorizontalPos else self.rect.center[0]
            newVerPos = mouseVerPos if isValidVerticalPos else self.rect.center[1]
            self.rect.center = (newHorPos, newVerPos)

    def handleSelect(self):
        if self.state == 'free': 
            #print(f'{self.__class__.__name__} selected!')
            self.state = 'selected'
            return self

    def handleDrop(self):
        if self.state == 'selected': 
            #print(f'{self.__class__.__name__} deselected!')
            self.state = 'free'
    
    def getColor(self):
        return self.color

    def isWhite(self):
        return self.color.name == 'white'

    def getOppositeColor(self):
        return PlayerColor.black if self.isWhite() else PlayerColor.white

    def destroy(self):
        self.kill()

    def addToOnXRay(self, labelPosFromAttackingPiece):
        self.onXRay.add(labelPosFromAttackingPiece)

    def clearOnXRay(self):
        self.onXRay = set()

    def isOnXRay(self):
        return len(self.onXRay)

    def isPiece(self, pieceName):
        return self.__class__.__name__ == pieceName

    @abstractmethod
    def posMove(self):
        pass

    @abstractmethod
    def getMovementMoves(self):
        pass

    @abstractmethod
    def getAttackMoves(self):
        pass

    @abstractmethod
    def getSpecialMoves(self):
        pass

    @abstractmethod
    def executeSpecialMove(self, board):
        pass

    @abstractmethod
    def validateSpecialMove(self, board):
        pass

