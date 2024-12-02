from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the `root` of a binary tree, return the preorder traversal of its nodes' values.
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        This function performs a preorder traversal of a binary tree
        Args:
        root (Optional[TreeNode]): The root of the binary tree

        Returns:
        List[int]: The preorder traversal of the binary tree
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result