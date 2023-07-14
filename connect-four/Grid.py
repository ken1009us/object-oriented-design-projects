from GridPosition import GridPosition


class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()


    def initGrid(self) -> None:
        self._grid = ([[GridPosition.EMPTY for _ in range(self._columns)]
                      for _ in range(self._rows)])


    def getGrid(self) -> list[list[GridPosition]]:
        return self._grid


    def getColumnCount(self) -> int:
        return self._columns


    def placePiece(self, column: int, piece: GridPosition) -> int:
        if column < 0 or column >= self._columns:
            raise ValueError('Invalid column!')
        if piece == GridPosition.EMPTY:
            raise ValueError('Invalid piece!')

        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row

        raise ValueError('Column is full!')


    def checkWin(self, connectN: int, row: int, column: int, piece: GridPosition) -> bool:
        count = 0
        # Check horizontal
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        count = 0
        # Check vertical
        for r in range(self._rows):
            if self._grid[r][column] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True


        # Check diagonal
        direction = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
        for dr, dc in direction:
            count = 0
            curRow, curCol = row, column
            while 0 <= curRow < self._rows and 0 <= curCol < self._columns:
                if self._grid[curRow][curCol] == piece:
                    count += 1
                else:
                    count = 0
                if count == connectN:
                    return True
                curRow += dr
                curCol += dc
        return False