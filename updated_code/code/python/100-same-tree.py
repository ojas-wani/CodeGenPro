from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This solution checks if two binary trees are the same.
    
    A binary tree is considered the same if it is structurally identical,
    and the nodes have the same value.

    Parameters:
    p (TreeNode): The root of the first binary tree.
    q (TreeNode): The root of the second binary tree.

    Returns:
    bool: True if the two binary trees are the same, False otherwise.
    """

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        This function checks if two binary trees are the same.

        Parameters:
        p (TreeNode): The root of the first binary tree.
        q (TreeNode): The root of the second binary tree.

        Returns:
        bool: True if the two binary trees are the same, False otherwise.
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)