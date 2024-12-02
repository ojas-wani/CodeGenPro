import java.util.Arrays;

/**
 * This class contains a method to calculate the mean of an array after removing the smallest 5% and the largest 5% of the elements.
 */
public class Solution {

    /**
     * This method calculates the mean of an array after removing the smallest 5% and the largest 5% of the elements.
     * 
     * @param arr the input array
     * @return the mean of the remaining elements
     */
    public double trimMean(int[] arr) {
        // Sort the array
        Arrays.sort(arr);
        
        // Calculate the length of the array
        final int len = arr.length;
        
        // Calculate the number of elements to remove
        final int count = (int) (len * 0.05);
        
        // Initialize the sum of the remaining elements
        int sum = 0;
        
        // Iterate over the middle part of the array
        for (int i = count; i < len - count; i++) {
            sum += arr[i];
        }
        
        // Return the mean of the remaining elements
        return (double) sum / (len - 2 * count);
    }
}