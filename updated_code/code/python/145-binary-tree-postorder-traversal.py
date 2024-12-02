from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    This class solves the postorder traversal of a binary tree.

    Args:
    root (Optional[TreeNode]): The root of the binary tree.

    Returns:
    List[int]: The postorder traversal of the binary tree.
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        This method performs the postorder traversal of the binary tree.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        List[int]: The postorder traversal of the binary tree.
        """
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]