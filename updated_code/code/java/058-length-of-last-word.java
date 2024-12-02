package improvedcodequality;

import java.util.Arrays;

/**
 * The LengthOfLastWord class is used to calculate the length of the last word in a given string.
 */
public class LengthOfLastWord {

    /**
     * The lengthOfLastWord method takes a string as input and returns the length of the last word.
     * 
     * @param s The input string.
     * @return The length of the last word.
     */
    public int lengthOfLastWord(String s) {
        // Trim the string to remove leading and trailing spaces
        String trimmedString = s.trim();

        // If the string is empty after trimming, return 0
        if (trimmedString.isEmpty()) {
            return 0;
        }

        // Split the string into an array of words using one or more spaces as the delimiter
        String[] words = trimmedString.split("\\s+");

        // Return the length of the last word
        return words[words.length - 1].length();
    }
}