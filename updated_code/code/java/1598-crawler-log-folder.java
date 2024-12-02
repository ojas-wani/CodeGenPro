package com.leetcoder;

import java.util.Stack;

public class Solution {
    public int minOperations(String[] logs) {
        int minOps = 0;
        Stack<Integer> depthStack = new Stack<>();

        for (String log : logs) {
            if (!log.equals("./")) {
                depthStack.push(1);
            } else if (!depthStack.isEmpty()) {
                depthStack.pop();
            }
        }

        while (!depthStack.isEmpty()) {
            depthStack.pop();
            minOps++;
        }

        return minOps;
    }
}