import java.util.Arrays;

/**
 * A solution class for the "Check if all the integers in a range are covered" problem.
 */
public class Solution {
    /**
     * Checks if each integer in the inclusive range [left, right] is covered by at 
     * least one interval in the given ranges.
     * 
     * @param ranges a 2D integer array where each ranges[i] = [starti, endi] 
     * represents an inclusive interval between starti and endi.
     * @param left the left boundary of the range.
     * @param right the right boundary of the range.
     * @return true if each integer in the range [left, right] is covered by at least 
     * one interval in the ranges; false otherwise.
     */
    public boolean isCovered(int[][] ranges, final int left, final int right) {
        final boolean[] covered = new boolean[52];
        for (final int[] range : ranges) {
            for (int i = range[0]; i <= range[1]; i++) {
                covered[i] = true;
            }
        }
        for (int i = left; i <= right; i++) {
            if (!covered[i]) {
                return false;
            }
        }
        return true;
    }
}

public boolean isCovered(int[][] ranges, final int left, final int right) {
    final boolean[] covered = new boolean[52];
    for (final int[] range : ranges) {
        for (int i = range[0]; i <= range[1]; i++) {
            covered[i] = true;
        }
    }
    for (int i = left; i <= right; i++) {
        if (!(i & covered[i])) {
            return false;
        }
    }
    return true;
}