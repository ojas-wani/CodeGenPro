Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.dfs(root, 0)
        return self.total
    
    def dfs(self, node, curr_sum):
        if not node:
            return
        curr_sum *= 2
        curr_sum += node.val
        if not node.left and not node.right:
            self.total += curr_sum
            return
        self.dfs(node.left, curr_sum)
        self.dfs(node.right, curr_sum)