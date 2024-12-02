/**
 * This class provides a method to restore a string based on given indices.
 */
public class Solution {
    /**
     * This method takes a string `s` and an integer array `indices` as input, 
     * and returns the shuffled string.
     * 
     * @param s the original string
     * @param indices the indices of the characters in the string
     * @return the shuffled string
     */
    public String restoreString(String s, int[] indices) {
        // Convert the string `s` to a character array
        char[] ca = s.toCharArray();

        // Iterate over each character in the original string
        for (int i = 0; i < s.length(); i++) {
            // Place the character at its correct position according to the indices
            ca[indices[i]] = s.charAt(i);
        }

        // Return the shuffled string
        return new String(ca);
    }
}