package com.example;

import java.util.Stack;

class Solution {
    /**
     * This class is used to solve the problem of maximum nesting depth of parentheses.
     *
     * @author <Your Name>
     */
    public int maxDepth(String s) {
        // Initialize the stack and maximum depth
        Stack<Integer> stack = new Stack<>();
        int maxDepth = 0;

        // Iterate over the string
        for (char c : s.toCharArray()) {
            // If the character is an opening parenthesis, push it onto the stack
            if (c == '(') {
                stack.push(1);
                // Update the maximum depth if necessary
                maxDepth = Math.max(maxDepth, stack.size());
            } else if (c == ')') {
                // If the stack is not empty, pop the opening parenthesis from the stack
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            }
        }

        // Return the maximum depth
        return maxDepth;
    }
}