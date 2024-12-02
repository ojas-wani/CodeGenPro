package exercises;
 
// Class comment is required
/**
 * This class contains a method to find any array containing n unique integers that sum up to 0.
 */
public class Solution {
 
    // Method comment is required
    /**
     * Finds any array containing n unique integers that sum up to 0.
     * 
     * @param n the number of unique integers in the array
     * @return an array containing n unique integers that sum up to 0
     */
    public int[] sumZero(int n) {
        int[] result = new int[n];
        for (int i = 1; i <= n / 2; i++) {
            result[i - 1] = i;
            if ((n & 1) == 1 && i == n / 2 + 1) {
                result[n / 2] = 0;
            } else {
                result[n - i] = -i;
            }
        }
        return result;
    }
}