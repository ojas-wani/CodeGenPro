package com.problem;

/**
 * Given an integer `n`, add a dot (".") as the thousands separator and return it in string format.
 */
public class Solution {
    /**
     * Add a dot (".") as the thousands separator and return it in string format.
     * 
     * @param n the input integer
     * @return the string with thousands separator
     */
    public String thousandSeparator(int n) {
        final String THOUSAND_SEPARATOR = ".";
        if (n < 1000) {
            return String.valueOf(n);
        }
        String str = String.valueOf(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            sb.append(str.charAt(i));
            if ((i + 1) % 3 == 0 && i != str.length() - 1) {
                sb.append(THOUSAND_SEPARATOR);
            }
        }
        return sb.toString();
    }
}