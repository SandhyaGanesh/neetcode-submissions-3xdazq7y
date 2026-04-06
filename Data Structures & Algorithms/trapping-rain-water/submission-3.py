class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        lMax = [0]*l
        rMax = [0]*l
        
        maxSoFar = height[0]
        for i in range(1,l):
            maxSoFar = max(maxSoFar, height[i-1])
            lMax[i] = maxSoFar
        
        maxSoFar = height[l-1]
        for i in range(l-2,-1, -1):
            maxSoFar = max(maxSoFar, height[i+1])
            rMax[i] = maxSoFar

        #print(lMax, rMax)
        totalWater = 0
        for i in range(1, l-1):
            h = min(lMax[i], rMax[i])
            w = (h - height[i]) if h > height[i] else 0
            #print(w)
            totalWater += w
        
        return totalWater
        