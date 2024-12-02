package my.packages;

/**
 * This class solves the problem of finding two integers a and b, 
 * where a and b are No-Zero integers (a and b do not contain any 0 in their decimal representation), 
 * and a + b = n.
 */
public class Solution {
    /**
     * Get No-Zero integers a and b, where a + b = n.
     * 
     * @param n a positive integer
     * @return a list of two integers [a, b] where a and b are No-Zero integers, 
     *         and a + b = n
     */
    public int[] getNoZeroIntegers(int n) {
        for (int i = 1; i < n; i++) {
            if (!String.valueOf(i).contains("0") && !String.valueOf(n - i).contains("0")) {
                return new int[]{i, n - i};
            }
        }
        return new int[]{}; // or throw an exception
    }
}