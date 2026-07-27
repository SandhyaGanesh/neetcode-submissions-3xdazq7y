class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        i = 0
        e = l - 1
        maxArea = 0

        while i < e:
            area = min(heights[i], heights[e])* (e-i)
            maxArea = max(area, maxArea)
            if heights[i] < heights[e]:
                i += 1
            else:
                e -= 1
        
        return maxArea