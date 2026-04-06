class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        stack = []
        maxArea = heights[0]

        for i in range(l):
            ip = i
            while stack and stack[-1][0] > heights[i]:
                hp, ip = stack.pop()
                maxArea = max(maxArea, (i-ip)*hp)
            stack.append((heights[i], ip))
        
        for hp, ip in stack:
            maxArea = max(maxArea, (l-ip)*hp)
        
        return maxArea
        
        
