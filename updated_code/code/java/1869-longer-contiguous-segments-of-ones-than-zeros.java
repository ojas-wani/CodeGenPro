//package declaration
package com problema;

import java.util.HashMap;
import java.util.Map;

/**
 * This class is for checking if the longest contiguous segment of 1s
 * is strictly longer than the longest contiguous segment of 0s in a binary string.
 */
public class Solution {
    /**
     * This method returns true if the longest contiguous segment of 1s
     * is strictly longer than the longest contiguous segment of 0s in a binary string,
     * or returns false otherwise.
     * 
     * @param s a binary string
     * @return whether the longest contiguous segment of 1s is strictly longer
     *         than the longest contiguous segment of 0s
     */
    public boolean checkZeroOnes(String s) {
        int maxOnes = 0, maxZeros = 0, currentOnes = 0, currentZeros = 0;

        Map<Character, Integer> currentSegment = new HashMap<>();
        int maxLength = 0;

        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentOnes++;
                currentZeros = 0;
            } else {
                currentZeros++;
                currentOnes = 0;
            }
            currentSegment.put(c, currentSegment.getOrDefault(c, 0) + 1);
            maxLength = Math.max(maxLength, currentSegment.get(c));
        }

        return maxLength > 0 && (maxOnes > maxZeros) || (maxOnes == maxZeros && maxOnes > 0);
    }
}