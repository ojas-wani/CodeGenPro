/**
 * This class contains a method that checks if an array of integers can be partitioned into three non-empty parts with equal sums.
 * 
 */
public class Solution {
    /**
     * This method checks if an array of integers can be partitioned into three non-empty parts with equal sums.
     * 
     * @param arr an array of integers
     * @return true if the array can be partitioned, false otherwise
     */
    public boolean canThreePartsEqualSum(int[] arr) {
        int totalSum = 0;
        for (int i = 0; i < arr.length; i++) {
            totalSum += arr[i];
        }
        if (totalSum % 3 != 0) {
            return false;
        }
        int targetSum = totalSum / 3;
        int count = 0;
        int currentSum = 0;
        for (int i = 0; i < arr.length; i++) {
            currentSum += arr[i];
            if (currentSum == targetSum) {
                count++;
                currentSum = 0;
            }
        }
        return count >= 2;
    }
}