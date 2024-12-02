// Package declaration
package com.pangram;

import java.util.Arrays;

/**
 * Solution for the pangram problem
 */
public class Solution {
    /**
     * Check if the sentence is a pangram
     * @param sentence the input sentence
     * @return true if the sentence is a pangram, false otherwise
     */
    public boolean checkIfPangram(String sentence) {
        boolean[] alphabetExist = new boolean[26]; // Assuming 26 English letters

        // Iterate through each character in the sentence
        for (char c : sentence.toCharArray()) {
            int index = c - 'a'; // Convert lowercase letter to index
            // If the character exists, mark its existence in the boolean array
            if (index >= 0 && index < 26) {
                alphabetExist[index] = true;
            }
        }

        // Check if all letters of the alphabet exist
        for (boolean exist : alphabetExist) {
            if (!exist) {
                return false; // If any letter doesn't exist, it's not a pangram
            }
        }

        return true; // If all letters exist, it's a pangram
    }
}