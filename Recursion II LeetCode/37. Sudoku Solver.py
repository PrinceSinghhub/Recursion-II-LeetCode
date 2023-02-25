class Solution:

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self._isSolve()

    def _checkRows(self, k, row):
        for i in range(9):
            if k == self.board[row][i]:
                return False
        return True

    def _checkCols(self, k, col):
        for i in range(9):
            if k == self.board[i][col]:
                return False
        return True

    def _checkBox(self, k, row, col):
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if self.board[i][j] == k:
                    return False
        return True

    def _isValid(self, row, col, k):
        boxRow = row - row % 3
        boxCol = col - col % 3
        return self._checkRows(k, row) and self._checkCols(k, col) and self._checkBox(k, boxRow, boxCol)

    def _findNextCell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def _isSolve(self):
        i, j = self._findNextCell()
        if i == -1 and j == -1:
            return True
        for k in range(1, 10):
            if self._isValid(i, j, str(k)):
                self.board[i][j] = str(k)
                if self._isSolve():
                    return True
                self.board[i][j] = '.'
        return False

ans = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(ans.solveSudoku(board))