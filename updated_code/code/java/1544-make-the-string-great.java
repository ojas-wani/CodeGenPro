package comsolution;

/**
 * This class solves the problem of making a string great by removing adjacent letters
 * that are the same but in different cases.
 */
public class Solution {

    /**
     * This method takes a string as an input and returns the string after making it great.
     * 
     * @param s the input string
     * @return the great string
     */
    public String makeGood(String s) {
        StringBuilder sb = new final StringBuilder();
        for (final char c : s.toCharArray()) {
            if (sb.length() > 0 && Character.toLowerCase(c) == Character.toLowerCase(sb.charAt(sb.length() - 1))
            		&& Character.toUpperCase(c) != Character.toUpperCase(sb.charAt(sb.length() - 1))) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}