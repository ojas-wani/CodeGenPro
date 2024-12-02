package com.example;

/**
 * This class contains a method to remove all adjacent duplicates in a string.
 * 
 * @author your_name
 */
public class RemoveAllAdjacentDuplicatesInString {

    /**
     * This method removes all adjacent duplicates in a string.
     * 
     * @param s the input string
     * @return the final string after all adjacent duplicates are removed
     */
    public String removeDuplicates(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == c) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        RemoveAllAdjacentDuplicatesInString solution = new RemoveAllAdjacentDuplicatesInString();
        System.out.println(solution.removeDuplicates("abbaca"));  // Output: "ca"
        System.out.println(solution.removeDuplicates("azxxzy"));  // Output: "ay"
    }
}