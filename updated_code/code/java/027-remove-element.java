package comCODE;
import java.util.Arrays;

/**
 * This is a Java class to remove all occurrences of a given value in a given array
 * in-place and return the number of elements in the array which are not equal to the given value.
 *
 * @author <your_name>
 */
public class Solution {
    /**
     * This method removes all occurrences of a given value in a given array in-place
     * and returns the number of elements in the array which are not equal to the given value.
     *
     * @param nums the input array
     * @param val  the value to remove
     * @return the number of elements in the array which are not equal to the given value
     */
    public int removeElement(int[] nums, int val) {
        // Checkstyle's "VariableName" rule is to use meaningful variable names
        int validIndex = 0;

        // Checkstyle's "MethodArgument" rule is to declare the parameters as final if they are not changed
        for (final int num : nums) {
            if (num != val) {
                nums[validIndex++] = num;
            }
        }
        // The array nums is now in-place modified and the validIndex tells the new size of the subarray
        return validIndex;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[] {3, 2, 2, 3};
        int val = 3;
        int k = solution.removeElement(nums, val);
        System.out.println(k);
        // Sort the first k elements of nums
        Arrays.sort(nums, 0, k);
        // Assert statement for validation
        for (int i = 0; i < k; i++) {
            System.out.println(nums[i]);
        }
    }
}