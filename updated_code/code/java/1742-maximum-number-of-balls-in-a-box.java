package org.example;

import java.util.HashMap;
import java.util.Map;

/**
 * This class is used to calculate the maximum number of balls in a box.
 */
public class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        // Initialize a HashMap to store the count of balls in each box.
        Map<Integer, Integer> boxCount = new HashMap<>();

        // Iterate through each ball from lowLimit to highLimit.
        for (int i = lowLimit; i <= highLimit; i++) {
            // Calculate the sum of digits of the ball's number.
            int sum = 0;
            int j = i;
            while (j != 0) {
                sum += j % 10;
                j /= 10;
            }

            // Increment the count of balls in the corresponding box.
            boxCount.put(sum, boxCount.getOrDefault(sum, 0) + 1);
        }

        // Return the maximum count of balls in a box.
        return boxCount.values().stream().max(Integer::compare).get();
    }
}