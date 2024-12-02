package com.example;

import java.util.Arrays;

/**
 * This class is used to determine if two halves of a string are alike.
 */
public class Solution {
    public boolean halvesAreAlike(String s) {
        // Check for empty string
        if (s.isEmpty()) {
            return true;
        }

        // Calculate the mid index
        int mid = s.length() / 2;

        // Split the string into two halves
        String half1 = s.substring(0, mid);
        String half2 = s.substring(mid);

        // Convert the strings to character arrays
        char[] chars1 = half1.toCharArray();
        char[] chars2 = half2.toCharArray();

        // Initialize the count of vowels in each half
        int count1 = 0;
        int count2 = 0;

        // Iterate through the character arrays
        for (char c : chars1) {
            // Check if the character is a vowel
            if (isVowel(c)) {
                count1++;
            }
        }
        for (char c : chars2) {
            if (isVowel(c)) {
                count2++;
            }
        }
        // Return if the counts of vowels are equal
        return count1 == count2;
    }

    private boolean isVowel(char c) {
        // Convert the character to lowercase
        c = Character.toLowerCase(c);
        // Check if the character is a vowel
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}