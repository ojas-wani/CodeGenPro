package com.check;

import java.util.regex.Pattern;

public class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        // Convert each word to numerical value
        int firstValue = numValue(firstWord);
        int secondValue = numValue(secondWord);
        int targetValue = numValue(targetWord);

        // Check if the sum of the numerical values of firstWord and secondWord equals the numerical value of targetWord
        return firstValue + secondValue == targetValue;
    }

    private int numValue(String word) {
        int value = 0;
        for (int i = 0; i < word.length(); i++) {
            value = value * 10 + (word.charAt(i) - 'a');
        }
        return value;
    }
}