/**
 * This class provides a solution to the problem of determining whether an array
 * can be rearranged to form an arithmetic progression.
 */
package LLMImprovedCodeQuality;

import java.util.Arrays;

/**
 * This class defines a method to determine whether an array can be rearranged
 * to form an arithmetic progression.
 */
public class CanMakeArithmeticProgression {
    /**
     * This method determines whether an array can be rearranged to form an arithmetic progression.
     * 
     * @param arr Array of numbers to check
     * @return true if the array can be rearranged to form an arithmetic progression, false otherwise
     */
    public boolean canMakeArithmeticProgression(int[] arr) {
        // Check if the array is empty
        if (arr.length < 2) {
            return true;
        }

        // Sort the array
        Arrays.sort(arr);

        // Calculate the initial difference
        int difference = arr[1] - arr[0];

        // Check if the difference is the same for all consecutive elements
        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] != difference) {
                return false;
            }
        }

        return true;
    }
}