# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.kCounter = 0
        self.res = 0
        self.k = 0

    def inOrderTraversal(self, root):
        if not root:
            return 
        
        self.inOrderTraversal(root.left)
        self.kCounter += 1
        if self.kCounter == k:
            self.res = root.val
        self.inOrderTraversal(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.k = k
        self.inOrderTraversal(root)
        return self.res
        