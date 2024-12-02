// Declare package name
package com.wanio.code;

import java.util.ArrayList;
import java.util.List;

/**
 * This class describes a solution for the problem of duplicating zeros in an array and shifting the rest of the elements to the right.
 * 
 * @author Wanio
 */
public class Solution {
    /**
     * This method duplicates each occurrence of zero in the given array and shifts the rest of the elements to the right.
     * 
     * @param arr the given array
     * @return void since the method modifies the array in place
     */
    public void duplicateZeros(int[] arr) {
        // Get the length of the array
        int length = arr.length;
        // Initialize the index from the end of the array
        int index = length - 1;
        
        // Iterate from the end of the array
        for (int i = length - 1; i >= 0; i--) {
            // If the current element is 0, make the element at the index 'index' also 0
            if (arr[i] == 0) {
                // Decrement the index if it's not the last element
                if (i < length - 1) {
                    arr[index] = 0;
                    index--;
                }
                // Set the element at the index 'index' to 0
                arr[index] = 0;
                index--;
            } else {
                // If the current element is not 0, copy its value to the index 'index'
                arr[index] = arr[i];
                index--;
            }
        }
    }
}