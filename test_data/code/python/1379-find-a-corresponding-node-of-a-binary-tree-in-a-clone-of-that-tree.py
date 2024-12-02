class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None
        self.copy(cloned, original, target)
        return self.result

    def copy(self, node, original, target):
        if node is None:
            return
        if node is target:
            self.result = node
            return
        self.copy(node.left, original, target)
        self.copy(node.right, original, target)