package com.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        // Initialize the result list
        List<Integer> result = new ArrayList<Integer>();

        // Initialize the stack
        Stack<TreeNode> stack = new Stack<TreeNode>();

        // Push the root node onto the stack
        if (root != null) {
            stack.push(root);
        }

        // Traverse the binary tree using a stack
        while (!stack.isEmpty()) {
            // Pop the top node from the stack
            TreeNode node = stack.pop();

            // Add the node's value to the result list
            result.add(node.val);

            // Push the node's left and right children onto the stack
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }

        // Reverse the result list to get the postorder traversal
        Collections.reverse(result);

        return result;
    }
}