# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDiameter = 0
        
        def maxDepth(root):
            nonlocal maxDiameter
            if not root:
                return 0
            mdLeft = maxDepth(root.left)
            mdRight = maxDepth(root.right)
            maxDiameter = max(maxDiameter, mdLeft+mdRight)
            return 1 + max(mdLeft, mdRight)

        maxDepth(root)
        return maxDiameter
        