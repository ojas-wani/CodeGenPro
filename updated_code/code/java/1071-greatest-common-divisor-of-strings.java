package com.question1071;

import java.util.Arrays;

/**
 * This class contains the solution to the problem described in problem 1071.
 */
public class Solution {
    /**
     * This method calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
     *
     * @param a the first number
     * @param b the second number
     * @return the GCD of a and b
     */
    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    /**
     * This method returns the largest string x such that x divides both str1 and str2.
     *
     * @param str1 the first string
     * @param str2 the second string
     * @return the largest string x such that x divides both str1 and str2
     */
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        int gcd = gcd(str1.length(), str2.length());
        return str1.substring(0, gcd);
    }
}