class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        startIdx = 0
        endIdx = l - 1
        res = 0

        while startIdx < endIdx:
            currVol = (endIdx - startIdx)* min(heights[startIdx], heights[endIdx])
            res = max(res, currVol)
            
            if heights[startIdx] < heights[endIdx]:
                startIdx += 1
            else:
                endIdx -= 1
        
        return res
        