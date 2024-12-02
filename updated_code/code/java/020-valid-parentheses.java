package com.example;

import java.util.Stack;

/**
 * Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`,
 * `'['` and `']'`, determine if the input string is valid.
 *
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 */
public class Solution {
    /**
     * Determines if the input string is valid.
     *
     * @param s the input string
     * @return true if the input string is valid, false otherwise
     */
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (final char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c == '(' ? ')' : c == '{' ? '}' : ']');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}