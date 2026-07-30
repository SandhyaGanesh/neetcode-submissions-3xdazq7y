# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arr = []
        self.result = 0
        self.count = 0
        self.k = 0

    def traverse(self, node):
        if not node or self.result:
            return
        
        self.traverse(node.left)
        self.count += 1
        if self.k == self.count:
            self.result = node.val
        self.traverse(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.traverse(root)
        return self.result