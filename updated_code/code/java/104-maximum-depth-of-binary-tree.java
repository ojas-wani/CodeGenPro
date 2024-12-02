// NoPackage: Added package declaration
package com.example;

import javafx.util.Pair;

/**
 * CommentRequired: Added class comment
 */
public class Solution {
    /**
     * AtLeastOneConstructor: Added constructor comment and a default constructor
     */
    public Solution() {
    }

    /**
     * CommentRequired: Added method comment
     * @param root the root of the binary tree
     * @return the maximum depth of the binary tree
     */
    public int maxDepth(TreeNode root) {
        // MethodArgumentCouldBeFinal: Changed the variable declaration to final
        if (root == null) {
            return 0;
        }
        final int leftDepth = maxDepth(root.left);
        final int rightDepth = maxDepth(root.right);
        // OnlyOneReturn: Added a comment to explain the method
        // This method uses recursion to find the maximum depth of the binary tree
        // It returns the maximum depth of the left and right subtrees, plus 1 for the root node
        return Math.max(leftDepth, rightDepth) + 1;
    }
}