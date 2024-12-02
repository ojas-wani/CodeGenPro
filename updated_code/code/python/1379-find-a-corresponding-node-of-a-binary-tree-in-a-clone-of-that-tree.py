class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, original, target):
            if node is None:
                return None
            if node is target:
                return node
            left = dfs(node.left, original, target)
            if left is not None:
                return left
            return dfs(node.right, original, target)

        return dfs(cloned, original, target)