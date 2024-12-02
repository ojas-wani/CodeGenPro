package com.issues;

/**
 * Class comments are required
 */
public class Solution {
    /**
     * Returns the index of the word in sentence where searchWord is a prefix of this word.
     * If searchWord is a prefix of more than one word, returns the index of the first word.
     * If there is no such word return -1.
     *
     * @param sentence   a string that consists of some words separated by a single space
     * @param searchWord a string that is being searched as a prefix of any word in sentence
     * @return the index of the word where searchWord is a prefix or -1 if not found
     */
    public int isPrefixOfWord(String sentence, String searchWord) {
        String[] words = sentence.split(" ");
        int i = 0;
        do {
            if (words[i].startsWith(searchWord)) {
                return i + 1;
            }
            i++;
        } while (i < words.length);
        return -1;
    }
}