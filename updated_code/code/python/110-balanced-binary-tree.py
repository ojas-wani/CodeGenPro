import typing as t

class TreeNode(t.Generic):
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: t.Optional[TreeNode]) -> bool:
        """
        Determine if the binary tree rooted at root is height-balanced.
        
        A tree is height-balanced if for every node in the tree, the difference between the height of the left and right subtree is at most 1.
        
        :param root: The root of the binary tree
        :return: True if the tree is height-balanced, False otherwise
        """
        if not root:
            return True
        
        def check_height(node: TreeNode) -> int:
            """
            Calculate the height of the subtree rooted at node.
            
            If the subtree is not height-balanced, return -1.
            
            :param node: The root of the subtree
            :return: The height of the subtree if it is height-balanced, -1 otherwise
            """
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1