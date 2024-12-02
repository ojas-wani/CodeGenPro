package LMImprovedCodeQuality;

/**
 * This class provides a method to find the square root of a given number.
 */
public class Solution {

    /**
     * Finds the integer square root of a given number.
     * 
     * @param x The number for which we need to find the integer square root.
     * @return The integer square root of the given number.
     */
    public int mySqrt(int finalX) {
        if (finalX == 0) {
            return 0;
        }

        int start = 1;
        int end = finalX;
        int mid = start;
        while (start <= end) {
            mid = start + (end - start) / 2;
            if (mid * mid == finalX) {
                return mid;
            } else if (mid * mid < finalX) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return end;
    }
}