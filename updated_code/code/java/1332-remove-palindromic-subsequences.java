package com.example;

import java.util.Scanner;

/**
 * This class contains the solution to the problem "1332 - Remove Palindromic Subsequences"
 *
 * @author Wanior
 */
public class RemovePalindromeSub {
    public int removePalindromeSub(String s) {
        int left = 0, right = s.length() - 1;
        // Check if the string is already a palindrome
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return 2;
            }
            left++;
            right--;
        }
        // If the string is a palindrome, return 1
        return 1;
    }

    public static void main(String[] args) {
        RemovePalindromeSub solution = new RemovePalindromeSub();
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        int result = solution.removePalindromeSub(s);
        System.out.println(result);
    }
}