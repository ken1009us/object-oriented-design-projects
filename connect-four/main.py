from Player import Player
from Grid import Grid
from GridPosition import GridPosition


class Game:
    def __init__(self, grid: Grid, connectN: int, targetScore: int) -> None:
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore
        self._players = [Player('Player 1', GridPosition.RED),
                         Player('Player 2', GridPosition.YELLOW)]
        self._score = {player.getName(): 0 for player in self._players}


    def printBoard(self) -> None:
        print('\nBoard:\n')
        grid = self._grid.getGrid()
        for row in grid:
            rowStr = ' '.join('R' if piece == GridPosition.RED else 'Y' if piece == GridPosition.YELLOW else '0' for piece in row)
            print(rowStr)
        print('')


    def playMove(self, player: Player) -> tuple[int, int]:
        self.printBoard()
        print(f"{player.getName()}'s turn...")
        colCnt = self._grid.getColumnCount()
        while True:
            try:
                moveColumn = int(input(f"Enter column between 1 and {colCnt} to add piece: ")) - 1
                moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
                return (moveRow, moveColumn)
            except (ValueError, IndexError):
                print("Invalid move! Please try again.")


    def playRound(self) -> Player:
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor) == True:
                    self._score[player.getName()] += 1
                    return player


    def play(self) -> None:
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round!")
            maxScore = max(self._score[winner.getName()], maxScore)
            self._grid.initGrid()

        print(f"{winner.getName()} won the game!")


def main():
    grid = Grid(6, 7)
    game = Game(grid, 4, 2)
    game.play()


if __name__ == '__main__':
    main()

