Python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solution class to check if a binary tree is symmetric.
    """
    
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        This function checks if the given binary tree is symmetric or not.
        
        Args:
        root (TreeNode): The root of the binary tree.
        
        Returns:
        bool: True if the binary tree is symmetric, False otherwise.
        """
        
        def is_mirror(t1, t2):
            """
            This function checks if two trees are mirror images of each other.
            
            Args:
            t1 (TreeNode): The root of the first tree.
            t2 (TreeNode): The root of the second tree.
            
            Returns:
            bool: True if the trees are mirror images, False otherwise.
            """
            
            if not t1 and not t2:
                # If both trees are empty, return True.
                return True
            if not t1 or not t2:
                # If one tree is empty and the other is not, return False.
                return False
            return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)
        
        return is_mirror(root.left, root.right)