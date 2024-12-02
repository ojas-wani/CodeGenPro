package com(LLM-Improved-Code-Quality.test_data.temp2.code.java);

import java.util.StringBuilder;

/**
 * This class provides a method to remove outermost parentheses of every primitive string in the primitive decomposition of a valid parentheses string.
 */
public class Solution {

    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int openCounter = 0;

        for (char c : s.toCharArray()) {
            if (c == '(' && openCounter > 0) {
                sb.append(c);
            } else if (c == ')') {
                if (openCounter > 0) {
                    sb.append(c);
                }
                openCounter--;
            } else {
                openCounter++;
                sb.append(c);
            }
        }

        return sb.toString();
    }
}