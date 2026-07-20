class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        smallerIndicesToTheLeft = [-1]*l
        smallerIndicesToTheRight = [l]*l
        stack = [(0, -1)]
        res = 0
        
        for i in range(l):
            h = heights[i]
            while stack and stack[-1][0] >= h:
                stack.pop()
            if stack:
                smallerIndicesToTheLeft[i] = stack[-1][1]
            stack.append((h, i))
        
        stack = [(0, l)]
        for i in range(l-1, -1, -1):
            h = heights[i]
            while stack and stack[-1][0] >= h:
                stack.pop()
            if stack:
                smallerIndicesToTheRight[i] = stack[-1][1]
            stack.append((h, i))
        
        
        # print(smallerIndicesToTheLeft, smallerIndicesToTheRight)
        for i in range(l):
            h = heights[i]
            res = max(res, h*(-1-smallerIndicesToTheLeft[i]+smallerIndicesToTheRight[i]))

        return res