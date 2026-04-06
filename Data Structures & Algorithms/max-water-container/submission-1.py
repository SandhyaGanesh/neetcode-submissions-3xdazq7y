class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = len(heights)
        s = 0
        e = l - 1
        while s < e:
            maxWater = max(maxWater, min(heights[s], heights[e])*(e-s))
            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
        return maxWater