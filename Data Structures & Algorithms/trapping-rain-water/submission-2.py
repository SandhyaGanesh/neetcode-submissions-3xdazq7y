class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftBoundary = height[l]
        rightBoundary = height[r]
        res = 0
        while l < r:
            if leftBoundary < rightBoundary:
                l += 1
                leftBoundary = max(height[l], leftBoundary)
                res += leftBoundary - height[l]
            else:
                r -= 1
                rightBoundary = max(height[r], rightBoundary)
                res += rightBoundary - height[r]
        return res
