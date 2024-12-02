package com.exercise.solution;

import java.util.ArrayList;
import java.util.List;

/**
 * A class to find occurrences of a bigram in a text
 */
public class Solution {
    /**
     * Finds occurrences of a bigram in a text and returns an array of third words
     * 
     * @param text the input text
     * @param first the first word of the bigram
     * @param second the second word of the bigram
     * @return an array of third words
     */
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        List<String> result = new ArrayList<>();
        
        for (int i = 0; i < words.length - 2; i++) {
            if (words[i].equals(first) && words[i + 1].equals(second)) {
                result.add(words[i + 2]);
            }
        }
        
        return result.toArray(new String[0]);
    }
}