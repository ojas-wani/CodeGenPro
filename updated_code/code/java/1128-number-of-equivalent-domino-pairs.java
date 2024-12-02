package com.example;

import java.util.HashMap;
import java.util.Map;

/**
 * This class is used to count the number of equivalent domino pairs.
 */
public class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        // Use a HashMap to store the count of each domino
        Map<String, Integer> map = new HashMap<>();
        for (int[] domino : dominoes) {
            // Create a key for the domino by sorting the values and joining them with a comma
            String key = String.format("%d,%d", Math.min(domino[0], domino[1]), Math.max(domino[0], domino[1]));
            // Increment the count for the key
            map.put(key, map.getOrDefault(key, 0) + 1);
        }

        int res = 0;
        for (int count : map.values()) {
            // Calculate the number of pairs for each count
            res += count * (count - 1) / 2;
        }
        return res;
    }
}