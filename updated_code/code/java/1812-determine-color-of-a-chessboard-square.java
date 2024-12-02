package chessboard;

import java.lang.String;

/**
 * This class determines whether a chessboard square is white or black.
 */
public class ChessboardSquare {

    /**
     * This method determines whether a chessboard square is white or black.
     * 
     * @param coordinates  a string representing the coordinates of a chessboard square
     * @return true if the square is white, false if the square is black
     */
    public boolean squareIsWhite(String coordinates) {
        // Declare col and row as final variables
        final char col = coordinates.charAt(0);
        final int row = Integer.parseInt(coordinates.substring(1));

        // Return true if the sum of the column number and the row number is odd
        return (col - 'a' + row) % 2 == 1;
    }
}