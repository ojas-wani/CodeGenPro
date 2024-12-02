package solution;

/**
 * Given a string columnTitle that represents the column title as appears in an
 * Excel sheet, return its corresponding column number.
 *
 * @author <author name>
 */
public class Solution {
    /**
     * Returns the column number corresponding to the given column title.
     *
     * @param columnTitle a string representing the column title in Excel sheet
     * @return the corresponding column number
     */
    public int titleToNumber(String columnTitle) {
        int res = 0;
        for (char c : columnTitle.toCharArray()) {
            // Declare c as final to avoid unnecessary re-calculation
            final int value = c - 'A' + 1;
            // Declare res as final to avoid unnecessary re-calculation
            final int temp = res;
            res = res * 26 + value;
        }
        return res;
    }
}