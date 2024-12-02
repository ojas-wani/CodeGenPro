package com.solution;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Reorders spaces between words to maximize the equal number of spaces.
 */
public class Solution {
    public String reorderSpaces(String text) {
        String trimmedText = text.trim();
        String[] words = trimmedText.split("\\s+");
        int totalSpaces = trimmedText.length() - trimmedText.replaceAll("\\s", "").length();
        int wordsCount = words.length;

        if (wordsCount == 1) {
            return words[0] + String.format("%-" + totalSpaces + "s", " ").replace(" ", "");
        }

        int spacesBetweenWords = totalSpaces / (wordsCount - 1);
        int leftOverSpaces = totalSpaces % (wordsCount - 1);

        StringBuilder result = new StringBuilder();
        for (String word : words) {
            result.append(word);
            if (result.length() < text.length()) {
                for (int i = 0; i < spacesBetweenWords; i++)
                    result.append(' ');
                if (leftOverSpaces > 0) {
                    result.append(' ');
                    leftOverSpaces--;
                }
            }
        }
        return result.toString();
    }
}