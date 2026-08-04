# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.currMax = 0
    def maxPathSumHelper(self, root):
        if not root:
            return 0
        if not root.right and not root.left:
            self.currMax = max(root.val, self.currMax)
            return root.val
        
        leftMax = max(self.maxPathSumHelper(root.left), 0)
        rightMax = max(self.maxPathSumHelper(root.right), 0)

        self.currMax = max(leftMax + root.val + rightMax, self.currMax, root.val + max(leftMax, rightMax))
        return root.val + max(leftMax, rightMax)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currMax = root.val
        self.maxPathSumHelper(root)
        return self.currMax