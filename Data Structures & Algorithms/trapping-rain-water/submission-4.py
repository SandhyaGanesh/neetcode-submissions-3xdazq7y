class Solution:
    def trap(self, heights: List[int]) -> int:
        maxHeight = max(heights)
        l = len(heights)
        water = 0
        
        i = 0
        maxSoFar = heights[i]
        while heights[i] < maxHeight:
            if heights[i] < maxSoFar:
                water += maxSoFar - heights[i]
            else:
                maxSoFar = heights[i]
            i += 1
        
        e = l - 1
        maxSoFar = heights[e]
        while heights[e] < maxHeight:
            if heights[e] < maxSoFar:
                water += maxSoFar - heights[e]
            else:
                maxSoFar = heights[e]
            e -= 1
        
        while i < e:
            water += maxHeight - heights[i]
            i += 1
        
        return water