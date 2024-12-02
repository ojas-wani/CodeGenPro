import java.util.Arrays;

public class Solution {
    /**
     * @param nums an integer array
     * @param k an integer
     * @return the largest possible sum of the array after modifying it in the way described
     */
    public int largestSumAfterKNegations(int[] nums, int k) {
        // Sort the array in ascending order
        Arrays.sort(nums);

        // Iterate through the array from the start to the end
        for (int i = 0; i < nums.length; i++) {
            // If the element is negative and k is greater than 0
            if (nums[i] < 0 && k > 0) {
                // Negate the element and decrement k
                nums[i] = -nums[i];
                k--;
                // If k is 0, break the loop
                if (k == 0) {
                    break;
                }
            }
        }

        // If k is still greater than 0, it means all elements are negative
        if (k > 0) {
            // Find the smallest positive number in the array
            int min = Integer.MAX_VALUE;
            for (int num : nums) {
                if (num > 0) {
                    min = Math.min(min, num);
                }
            }
            // Negate the smallest positive number k times
            for (int i = 0; i < k; i++) {
                min = -min;
            }
            // Sum up all elements in the array
            int sum = 0;
            for (int num : nums) {
                sum += num;
            }
            // Add the negated smallest positive number
            sum += min;
        } else {
            // Simply sum up all elements in the array
            int sum = 0;
            for (int num : nums) {
                sum += num;
            }
        }
        return sum;
    }
}