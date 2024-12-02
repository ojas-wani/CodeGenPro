package solutions;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    /**
     * This method finds the index of the first occurrence of a given pattern in a string.
     * 
     * @param haystack The string in which we are searching for the pattern.
     * @param needle   The pattern that we are searching for in the string.
     * @return The index of the first occurrence of the pattern in the string, or -1 if the pattern is not found.
     */
    public int strStr(String haystack, String needle) {
        // Base case: if the needle is empty, we return 0
        if (needle.isEmpty()) {
            return 0;
        }

        // Create a regex pattern that matches the needle
        Pattern pattern = Pattern.compile(needle);

        // Search for the pattern in the haystack
        Matcher matcher = pattern.matcher(haystack);

        // If the pattern is found, return the starting index of the match
        if (matcher.find()) {
            return matcher.start();
        }

        // If the pattern is not found, return -1
        return -1;
    }
}