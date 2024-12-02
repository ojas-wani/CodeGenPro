class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        for i, move in enumerate(moves):
            row, col = move
            grid[row][col] = 'X' if i % 2 == 0 else 'O'
            if self.check_win(grid, 'X'):
                return 'A'
            if self.check_win(grid, 'O'):
                return 'B'
            if i == len(moves) - 1:
                return 'Draw'
        
        return 'Pending'

    def check_win(self, grid, player):
        for row in grid:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(grid[row][col] == player for row in range(3)):
                return True
        if all(grid[i][i] == player for i in range(3)):
            return True
        if all(grid[i][2 - i] == player for i in range(3)):
            return True
        return False