/**
 * Class to find the largest lucky integer in an array.
 */
package com.example;

public class Solution {
    /**
     * Method to find the largest lucky integer in an array.
     *
     * @param arr an array of integers
     * @return the largest lucky integer in the array, -1 if no lucky integer exists
     */
    public int findLucky(int[] arr) {
        // Create a frequency map to store the frequency of each number
        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : arr) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        // Initialize the result as -1
        int result = -1;
        for (int num : arr) {
            // Check if the frequency of the number is equal to the number itself
            if (frequency.get(num) == num) {
                // Update the result as the maximum of the current result and the lucky number
                result = Math.max(result, num);
            }
        }
        return result;
    }
}