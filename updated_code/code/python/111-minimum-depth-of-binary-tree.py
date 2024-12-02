Python
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This class represents the solution for the problem of finding the minimum depth of a binary tree.
    """

    """
    The docstring for this class should describe what the class does, its methods, and its structure.
    """
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        This method calculates the minimum depth of a binary tree.
        
        Args:
        root (Optional[TreeNode]): The root of the binary tree.
        
        Returns:
        int: The minimum depth of the binary tree.
        """
        
        if not root:  # If the tree is empty, return 0
            return 0
        
        queue = deque([(root, 1)])  # Initialize a queue with the root node and its depth
        
        while queue:
            node, depth = queue.popleft()  # Dequeue the next node and its depth
            
            if not node.left and not node.right:  # If the node is a leaf, return its depth
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))  # Enqueue the left child and its depth
            if node.right:
                queue.append((node.right, depth + 1))  # Enqueue the right child and its depth

# Your input should be in the following format:
# root = [3,9,20,null,null,15,7]
# Your output should be:
# 2