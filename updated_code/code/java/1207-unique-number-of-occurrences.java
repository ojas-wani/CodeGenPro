/**
 * This is a solution to the problem of checking if the number of occurrences
 * of each value in the array is unique.
 * 
 */
package com.coding.challenges;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     * Returns true if the number of occurrences of each value in the array is unique, 
     * and false otherwise.
     * 
     * @param arr The input array.
     * @return Whether the number of occurrences is unique.
     */
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            if (!countMap.containsKey(num)) {
                countMap.put(num, 0);
            }
            countMap.put(num, countMap.get(num) + 1);
        }

        int count = 0;
        int frequencyCount = 0;
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > 0) {
                count++;
                for (Map.Entry<Integer, Integer> existingEntry : countMap.entrySet()) {
                    if (existingEntry.getKey() != entry.getKey() && existingEntry.getValue() == entry.getValue()) {
                        return false;
                    }
                }
                frequencyCount++;
            }
        }

        return frequencyCount == count;
    }
}