# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lSum = self.maxDepthSum(root.left)
        rSum = self.maxDepthSum(root.right)
        
        return max(lSum, rSum, 0) + root.val

        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1000001

        lSum = self.maxPathSum(root.left)
        iSum = max(self.maxDepthSum(root.left), self.maxDepthSum(root.left) + self.maxDepthSum(root.right), self.maxDepthSum(root.right), 0) + root.val 
        rSum = self.maxPathSum(root.right)

        return max(lSum, iSum, rSum)