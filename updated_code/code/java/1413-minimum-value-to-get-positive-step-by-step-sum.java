package solver;
/**
 * Provides a solution to find the minimum positive value of _startValue_ 
 * such that the step by step sum is never less than 1.
 */
public class Solution {
    /**
     * Method to find the minimum positive value of _startValue_ 
     * such that the step by step sum is never less than 1.
     * 
     * @param nums an array of integers
     * @return the minimum positive value of _startValue_
     */
    public int minStartValue(int[] nums) {
        int sum = 0;
        int minStartValue = 0;

        for (int num : nums) {
            final int tempNum = num;
            sum += num;
            minStartValue = Math.max(minStartValue, 1 - sum);
        }

        return Math.max(minStartValue, 1);
    }
}