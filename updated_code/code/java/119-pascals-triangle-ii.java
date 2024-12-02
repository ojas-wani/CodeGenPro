import java.util.ArrayList;
import java.util.List;

/**
 * This class calculates the `rowIndexth` (0-indexed) row of Pascal's triangle.
 */
public class Solution {
    /**
     * Calculate the `rowIndexth` (0-indexed) row of Pascal's triangle.
     * 
     * @param rowIndex - The index of the row in Pascal's triangle.
     * @return The `rowIndexth` row of Pascal's triangle.
     */
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        row.add(1);
        if (rowIndex == 0) {
            return row;
        }
        row.add(1);
        for (int i = 2; i <= rowIndex; i++) {
            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);
            for (int j = 1; j < i; j++) {
                newRow.add(row.get(j - 1) + row.get(j));
            }
            newRow.add(1);
            row = newRow;
        }
        return row;
    }
}