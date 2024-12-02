import java.util.*;

public class Solution {
    /**
     * Returns the count of odd numbers between low and high (inclusive).
     * 
     * @param low   The lower bound of the range.
     * @param high  The upper bound of the range.
     * @return      The count of odd numbers in the range.
     */
    public int countOdds(int low, int high) {
        // Check if the range is empty
        if (low > high) {
            return 0;
        }

        // Calculate the count of odd numbers in the range
        int oddCount = (high - low) / 2 + (high % 2 == 1 ? 1 : 0);

        return oddCount;
    }
}