package com.example;

import java.util.Arrays;

public class Solution {
    /**
     * Given a string text, use the characters of text to form as many instances
     * of the word "balloon" as possible.
     * 
     * @param text the input string
     * @return the maximum number of instances that can be formed
     */
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[5];
        boolean[] alphabet = new boolean[26];

        // Count characters in text
        for (char c : text.toLowerCase().toCharArray()) {
            if (c == 'b') counts[0]++;
            else if (c == 'a') counts[1]++;
            else if (c == 'l') {
                counts[2]++;
                alphabet['l' - 'a'] = true;
            }
            else if (c == 'o') {
                counts[3]++;
                alphabet['o' - 'a'] = true;
            }
            else if (c == 'n') {
                counts[4]++;
                alphabet['n' - 'a'] = true;
            }
        }

        // "balloon" has 2 L's, 2 O's
        counts[2] /= 2;
        counts[3] /= 2;

        // get the number of each distinct letter in "balloon"
        int[] balloonLetters = {0, 0, 2, 2, 1};
        for (int i = 0; i < 26; i++) {
            balloonLetters[i] = (alphabet[i] ? 1 : 0);
        }

        // find the min count of each character
        int minCount = Integer.MAX_VALUE;
        for (int i = 0; i < 5; i++) {
            minCount = Math.min(minCount, Math.min(counts[i], balloonLetters[i]));
        }
        return minCount;
    }
}