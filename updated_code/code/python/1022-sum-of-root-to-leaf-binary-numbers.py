from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This class is used to solve the problem of finding the sum of all binary numbers from root to leaf.
    """
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        This function calculates the sum of all binary numbers from root to leaf.
        """
        self.total = 0
        self.dfs(root, 0)
        return self.total
    
    def dfs(self, node, curr_sum):
        """
        This function performs a depth-first search on the binary tree.
        """
        if not node:
            return
        curr_sum = curr_sum * 2 + node.val
        if not node.left and not node.right:
            self.total += curr_sum
        else:
            self.dfs(node.left, curr_sum)
            self.dfs(node.right, curr_sum)