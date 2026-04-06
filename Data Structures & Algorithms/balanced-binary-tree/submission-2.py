# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        isNotBalanced = False

        def maxDepth(root):
            nonlocal isNotBalanced
            if not root:
                return 0
            mdLeft = maxDepth(root.left)
            mdRight = maxDepth(root.right)
            if not (-1 <= mdLeft - mdRight <= 1):
                isNotBalanced = True
            return 1 + max(mdLeft, mdRight)

        maxDepth(root)
        return True if not isNotBalanced else False