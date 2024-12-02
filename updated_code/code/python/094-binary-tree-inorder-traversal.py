from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This class provides a solution for the binary tree inorder traversal problem.
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        This function performs the inorder traversal of the binary tree.
        :param root: The root of the binary tree.
        :return: A list of node values in the order they were visited.
        """
        # Create a stack to store nodes and initialize an empty list to store the result
        stack = deque()
        result = []
        
        # Iterate over the tree using theMorris traversal algorithm
        current = root
        while True:
            if current:
                # Traverse to the leftmost node in the current subtree
                while current.left:
                    stack.append(current)
                    current = current.left
                # Visit the node and move to its right subtree
                result.append(current.val)
                current = current.right
            elif stack:
                # Move to the next node from the stack
                top_node = stack.pop()
                current = top_node.right
            else:
                break
        
        return result