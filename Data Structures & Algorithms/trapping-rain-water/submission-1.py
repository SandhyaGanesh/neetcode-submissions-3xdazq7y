class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        maxHeight = max(height)
        firstMax = 0
        for i in range(l):
            if height[i] == maxHeight:
                firstMax = i
                break
        lastMax = 0
        for i in range(l-1, -1, -1):
            if height[i] == maxHeight:
                lastMax = i
                break
        
        if l == 1:
            return 0
        
        water = 0
        maxSoFar = height[0]
        for i in range(0,firstMax):
            maxSoFar = max(maxSoFar, height[i])
            water += maxSoFar-height[i]
        for i in range(firstMax, lastMax):
            water += height[firstMax]-height[i]
        maxSoFar = height[-1]
        for i in range(l-1,lastMax,-1):
            maxSoFar = max(maxSoFar, height[i])
            water += maxSoFar-height[i]

        return water