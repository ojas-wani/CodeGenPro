import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {
    /**
     * Definition for a binary tree node.
     * public class TreeNode {
     *     int val;
     *     TreeNode left;
     *     TreeNode right;
     *     TreeNode() {}
     *     TreeNode(int val) { this.val = val; }
     *     TreeNode(int val, TreeNode left, TreeNode right) {
     *         this.val = val;
     *         this.left = left;
     *         this.right = right;
     *     }
     * }
     */
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        // Fix: add a package declaration
        package com.example;

        /**
         * Fix: add a constructor comment
         */
        public Solution() {}

        /**
         * Fix: add a comment for the method
         */
        public List<Integer> inorderTraversal(TreeNode root) {
            // Fix: add a comment for the variable
            List<Integer> result = new ArrayList<>();

            // Fix: add a comment for the variable
            Stack<TreeNode> stack = new Stack<>();
            TreeNode current = root;

            while (current != null || !stack.isEmpty()) {
                while (current != null) {
                    // Fix: add a comment for the variable
                    stack.push(current);
                    current = current.left;
                }
                current = stack.pop();
                result.add(current.val);
                current = current.right;
            }
            return result;
        }
    }
}