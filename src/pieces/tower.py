from pieces.piece import Piece

class Tower(Piece): 

    def __init__(self, color, startPosition):
        super().__init__(color, startPosition)
        print('pawn')
    
    def move():
        print('move')

    def attack():
        print('atk')