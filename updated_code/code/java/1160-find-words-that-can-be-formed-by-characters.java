package com.lbmsoft.lean.code;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int countCharacters(String[] words, String chars) {
        if (chars == null) {
            throw new NullPointerException("chars is null");
        }

        // Create a frequency map for the characters in 'chars'
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : chars.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        int goodLength = 0;
        for (String word : words) {
            // Create a frequency map for the characters in 'word'
            Map<Character, Integer> wordCount = new HashMap<>();
            for (char c : word.toCharArray()) {
                wordCount.put(c, wordCount.getOrDefault(c, 0) + 1);
            }

            boolean isGood = true;
            for (Map.Entry<Character, Integer> entry : wordCount.entrySet()) {
                if (!charCount.containsKey(entry.getKey()) || entry.getValue() > charCount.get(entry.getKey())) {
                    isGood = false;
                    break;
                }
            }
            if (isGood) {
                goodLength += word.length();
            }
        }
        return goodLength;
    }
}