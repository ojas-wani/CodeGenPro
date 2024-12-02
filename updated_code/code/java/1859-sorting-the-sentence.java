/**
 * This class contains a single method to reconstruct a shuffled sentence from a given string.
 */
package com.ww.code;

import java.util.*;

public class Solution {

    /**
     * Sorts the shuffled sentence based on word positions and returns the original sentence.
     * 
     * @param s the shuffled sentence
     * @return the original sentence
     */
    public String sortSentence(String s) {
        // Split the input string into words
        String[] words = s.split(" ");
        
        // Sort the words based on their positions (last character of each word)
        Arrays.sort(words, (a, b) -> Integer.parseInt(a.substring(a.length() - 1)) - Integer.parseInt(b.substring(b.length() - 1)));
        
        // Initialize a StringBuilder to construct the original sentence
        StringBuilder sb = new StringBuilder();
        
        // Iterate through the sorted words and append them to the StringBuilder
        for (String word : words) {
            sb.append(word.substring(0, word.length() - 1)).append(" ");
        }
        
        // Trim the StringBuilder to remove trailing spaces and return the result
        return sb.toString().trim();
    }
}