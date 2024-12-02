package com.codeiq;

/**
 * This class contains the method to find the maximum score after splitting a string into two non-empty substrings.
 */
public class MaxScore {
    /**
     * This method calculates the maximum score after splitting a string into two non-empty substrings.
     * 
     * @param s the input string
     * @return the maximum score
     */
    public int maxScore(String s) {
        int max = 0;

        // Count the number of zeros and ones in the left substring
        int zeros = 0, ones = 0;

        // Count the number of zeros and ones in the right substring
        int rightZeros = 0, rightOnes = 0;

        // Count the number of ones in the right part of the string
        int rightOnesCount = 0;
        
        // Count the number of ones and zeros in the string
        int onesCount = 0, zerosCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                onesCount++;
                ones++;
            } else {
                zerosCount++;
                zeros++;
            }
        }

        // Iterate over the string to count the number of ones and zeros in the right part
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '1') {
                rightOnesCount++;
                rightOnes++;
            } else {
                rightZeros++;
            }
        }

        // Calculate the score for each possible split
        for (int i = 1; i < s.length(); i++) {
            rightOnesCount -= s.charAt(i - 1) == '1' ? 1 : 0;
            rightZeros += s.charAt(i - 1) == '0' ? 1 : 0;
            max = Math.max(max, zeros + rightOnes);
        }

        return max;
    }
}