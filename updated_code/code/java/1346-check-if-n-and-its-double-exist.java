package com.example;

/**
 * This class is used to check if there exist two indices i and j in the given array such that:
 * i != j
 * 0 <= i, j < arr.length
 * arr[i] == 2 * arr[j]
 */
public class CheckIfExist {
    /**
     * This method checks if there exist two indices i and j in the given array such that:
     * i != j
     * 0 <= i, j < arr.length
     * arr[i] == 2 * arr[j]
     * 
     * @param arr an array of integers
     * @return true if there exist two indices i and j that satisfy the conditions, otherwise false
     */
    public boolean checkIfExist(int[] arr) {
        // Declare set and num as final
        final Set<Integer> set = new HashSet<>();
        final int[] inputArray = arr;

        for (final int num : inputArray) {
            // Declare num as final
            final int currentNumber = num;

            if ((currentNumber % 2 == 0 && set.contains(currentNumber / 2)) || set.contains(currentNumber * 2)) {
                return true;
            }
            set.add(currentNumber);
        }
        return false;
    }
}