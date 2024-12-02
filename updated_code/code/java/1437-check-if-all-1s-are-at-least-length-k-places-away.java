package checkIfAll1sAreAtLeastLengthKPlacesAway;

import java.util.Arrays;

class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        // Initialize the index to the start of the array
        int index = 0;
        
        // Loop through the array
        while (index < nums.length) {
            // If the current index is not a '1' increment the index
            if (nums[index] != 1) {
                index++;
            } else if (index + 1 < k) {
                // If we are at a '1' and it's less than 'k' places away, return false
                return false;
            } else {
                // If we are at a '1' and it's 'k' places away or more, we can skip the next 'k' indices
                index += k;
            }
        }
        // If we have reached the end of the array without finding an adjacent '1', return true
        return true;
    }
}

package checkIfAll1sAreAtLeastLengthKPlacesAway;

/**
 * This class provides a solution to the checkIfAll1sAreAtLeastLengthKPlacesAway problem.
 */
public class Solution {
    /**
     * Constructor for the Solution class.
     */
    public Solution() {
    }

    /**
     * This method checks if all ones are at least length k places away from each other.
     *
     * @param nums  The binary array.
     * @param k     The length of distance between two ones.
     * @return true if all ones are at least length k places away from each other, false otherwise.
     */
    public boolean kLengthApart(int[] nums, int k) {
        // Initialize the index to the start of the array
        int index = 0;
        
        // Loop through the array
        while (index < nums.length) {
            // If the current index is not a '1' increment the index
            if (nums[index] != 1) {
                index++;
            } else if (index + 1 < k) {
                // If we are at a '1' and it's less than 'k' places away, return false
                return false;
            } else {
                // If we are at a '1' and it's 'k' places away or more, we can skip the next 'k' indices
                index += k;
            }
        }
        // If we have reached the end of the array without finding an adjacent '1', return true
        return true;
    }
}