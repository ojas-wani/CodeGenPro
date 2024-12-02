import java.util.Arrays;

public class Solution {
    public String tictactoe(int[][] moves) {
        String[][] grid = new String[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                grid[i][j] = " ";
            }
        }
        String result = "Pending";
        for (int i = 0; i < moves.length; i++) {
            int row = moves[i][0];
            int col = moves[i][1];
            if (i % 2 == 0) {
                grid[row][col] = "X";
            } else {
                grid[row][col] = "O";
            }
            if (checkWin(grid, "X")) {
                result = "A";
                break;
            } else if (checkWin(grid, "O")) {
                result = "B";
                break;
            } else if (checkDraw(grid)) {
                result = "Draw";
                break;
            }
        }
        return result;
    }

    public boolean checkWin(String[][] grid, String player) {
        // Check rows
        for (int i = 0; i < 3; i++) {
            if (grid[i][0].equals(player) && grid[i][1].equals(player) && grid[i][2].equals(player)) {
                return true;
            }
        }
        // Check columns
        for (int i = 0; i < 3; i++) {
            if (grid[0][i].equals(player) && grid[1][i].equals(player) && grid[2][i].equals(player)) {
                return true;
            }
        }
        // Check diagonals
        if ((grid[0][0].equals(player) && grid[1][1].equals(player) && grid[2][2].equals(player)) ||
                (grid[0][2].equals(player) && grid[1][1].equals(player) && grid[2][0].equals(player))) {
            return true;
        }
        return false;
    }

    public boolean checkDraw(String[][] grid) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j].equals(" ")) {
                    return false;
                }
            }
        }
        return true;
    }
}