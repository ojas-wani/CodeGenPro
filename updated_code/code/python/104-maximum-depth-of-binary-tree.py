from typing import Optional

class Solution:
    """
    This class provides a solution to find the maximum depth of a binary tree.

    Attributes:
        root (Optional[TreeNode]): The root node of the binary tree.
    """
    def max_depth(self, root: Optional['TreeNode']) -> int:
        """
        Returns the maximum depth of the binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree.

        Raises:
            None
        """
        if root is None:
            return 0
        else:
            left_depth = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            return max(left_depth, right_depth) + 1