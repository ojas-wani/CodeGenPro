import java.util.Arrays;

public class Solution {
    /**
     * Returns the number of **consistent** strings in the array `words`.
     * 
     * @param allowed   a string consisting of **distinct** characters
     * @param words     an array of strings
     * @return  the number of **consistent** strings in the array `words`
     */
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        // Convert the allowed string to a Set for efficient lookup
        char[] allowedArray = allowed.toCharArray();
        boolean[] allowedSet = new boolean[256];
        for (char c : allowedArray) {
            allowedSet[(int) c] = true;
        }

        // Iterate over each word in the array
        for (String word : words) {
            // Convert the word to a character array
            char[] wordArray = word.toCharArray();
            // Assume the word is consistent until we find a character not in allowed
            boolean isConsistent = true;
            for (char c : wordArray) {
                // Check if the character is in the allowed set
                if (!allowedSet[(int) c]) {
                    isConsistent = false;
                    break;
                }
            }
            // If the word is consistent, increment the count
            if (isConsistent) {
                count++;
            }
        }
        return count;
    }
}