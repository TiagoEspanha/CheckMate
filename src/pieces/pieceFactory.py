from constants import PlayerColor
from pieces.pawn import Pawn
from pieces.tower import Tower
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King

class PieceFactory():
    @staticmethod
    def _getPieceByLabel(label):
        pieceByLabel = {
            'P': Pawn,
            'R': Tower,
            'B': Bishop,
            'N': Knight,
            'Q': Queen,
            'K': King,
            '-': None,
        }
        return pieceByLabel[label]

    @staticmethod
    def _getPieceColorByLabel(label):
        pieceColorByLabel = {
            'b': PlayerColor.black,
            'w': PlayerColor.white,
            '-': None
        }
        return pieceColorByLabel[label]

    @staticmethod
    def buildByPositionLabel(posLabel):
        pieceColor = PieceFactory._getPieceColorByLabel(posLabel[0])
        pieceClass = PieceFactory._getPieceByLabel(posLabel[1])
            
        if(pieceClass and pieceColor):
            return pieceClass(pieceColor)