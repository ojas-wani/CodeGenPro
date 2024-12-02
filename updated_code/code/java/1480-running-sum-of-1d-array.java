/**
 * @author Your Name
 * @since 2023-02-22
 */
package code;

public class Solution {

    /**
     * Given an array `nums`. We define a running sum of an array as `runningSum[i] =
     * sum(nums[0]…nums[i])`.
     * 
     * @param nums the input array
     * @return the running sum of `nums`
     */
    public int[] runningSum(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = nums[0]; // consider using varargs for this method
        for (int i = 1; i < nums.length; i++) { // consider declaring 'i' as final
            result[i] = result[i - 1] + nums[i]; // consider adding a space after '+'
        }
        return result;
    }
}