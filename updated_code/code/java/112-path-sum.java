package solution;

import solution.TreeNode;

/**
 * This is a class to solve the Path Sum problem in a Binary Tree.
 * 
 * @author Your Name
 */
public class Solution {
    /**
     * This method checks if there is a root-to-leaf path in the binary tree with the given target sum.
     * 
     * @param root the root of the binary tree
     * @param targetSum the target sum
     * @return true if there is a path with the target sum, false otherwise
     */
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        targetSum -= root.val;
        if (root.left == null && root.right == null) {
            return targetSum == 0;
        }
        
        // Use braces to ensure code flow control
        if (root.left != null) {
            if (!hasPathSum(root.left, targetSum)) {
                return false;
            }
        }
        if (root.right != null) {
            if (!hasPathSum(root.right, targetSum)) {
                return false;
            }
        }
        
        return true;
    }
}