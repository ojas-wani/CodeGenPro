import java.util.Arrays;

public class Solution {
    /**
     * This method determines whether it's possible to make all strings in the input array equal using the given operations.
     * 
     * @param words an array of strings
     * @return true if it's possible to make all strings equal, false otherwise
     */
    public boolean makeEqual(String[] words) {
        int[] charCount = new int[26]; // Count the occurrences of each character
        int totalChars = 0; // Total number of characters in all strings

        // Count the total number of characters and count the occurrences of each character
        for (String word : words) {
            int[] wordCount = new int[26]; // Count the occurrences of each character in the current word
            for (char c : word.toCharArray()) {
                wordCount[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                charCount[i] += wordCount[i];
            }
            totalChars += word.length();
        }

        // Check if all strings can be made equal
        for (int count : charCount) {
            if (count % (totalChars / words.length) != 0) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Package comment for Solution package.
 * 
 * @author [Your Name]
 */
package Solution;