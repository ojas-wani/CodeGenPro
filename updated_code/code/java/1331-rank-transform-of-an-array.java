package com.wanio.Solution;

import java.util.*;

class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // Add a comment to explain the method
        // This method transforms the given array into a rank-based array
        Arrays.sort(arr);
        Map<Integer, Integer> rankMap = new HashMap<>();
        rankMap.put(arr[0], 1);
        int currentRank = 1;

        // Add a comment to explain the for loop
        // This loop creates a map to store the elements of the array along with their ranks
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1]) {
                // Check if the current element is different from the previous one
                currentRank++;
            }
            rankMap.put(arr[i], currentRank);
        }

        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            // Assign the element's rank to the result array
            result[i] = rankMap.get(arr[i]);
        }
        return result;
    }
}