from typing import List

class Solution:
    """
    This class implements a solution for the Tic Tac Toe game.
    """

    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        This method determines the winner of the Tic Tac Toe game given the moves.
        
        Args:
        moves (List[List[int]]): A 2D integer array where moves[i] = [rowi, coli] indicates the ith move.
        
        Returns:
        str: The winner of the game if it exists, "Draw" if the game ends in a draw, "Pending" if there are still movements to play.
        """

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
        """
        This method checks if there is a winner in the game.
        
        Args:
        grid (List[List[str]]): The current state of the game.
        player (str): The player to check for a win.
        
        Returns:
        bool: True if the player has won, False otherwise.
        """

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