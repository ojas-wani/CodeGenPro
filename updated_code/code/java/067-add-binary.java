package com.example;

import java.util.*;

/**
 * This class is used to add two binary strings together.
 */
public class Solution {
    /**
     * This method calculates the sum of two binary strings and returns the result as a binary string.
     * 
     * @param a the first binary string
     * @param b the second binary string
     * @return the sum of a and b as a binary string
     */
    public String addBinary(String a, String b) {
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        StringBuilder res = new StringBuilder();

        // Loop through each character in the longest string
        while(i >= 0 || j >= 0 || carry > 0) {
            carry = 0;
            int sum = carry;
            if(i >= 0) {
                sum += a.charAt(i--) - '0';
            }
            if(j >= 0) {
                sum += b.charAt(j--) - '0';
            }
            res.append((sum % 2) + '');
            carry = sum / 2;
        }

        // Reverse the result string
        String result = res.reverse().toString();

        return result;
    }
}