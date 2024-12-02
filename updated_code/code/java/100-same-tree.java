package com.code;

import com.code.TreeNode;

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Ensure the file ends with a newline.
        if (p == null && q == null) {
            return true;
        }
        
        // Ensure the file does not contain unresolved references.
        if (p == null || q == null) {
            return false;
        }
        
        // Ensure the file does not contain type mismatches.
        if (p.val != q.val) {
            return false;
        }
        
        // Ensure the file does not contain unclear logic.
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}