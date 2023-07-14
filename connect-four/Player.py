from GridPosition import GridPosition


class Player:
    def __init__(self, name: str, pieceColor: GridPosition) -> None:
        self._name = name
        self._pieceColor = pieceColor

    def getName(self):
        return self._name

    def getPieceColor(self):
        return self._pieceColor