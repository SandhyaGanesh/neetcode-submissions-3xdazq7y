class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        left = [0] * l
        right = [0] * l

        stack = []
        for i in range(l - 1, -1, -1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if stack:
                index = stack[-1][0]
                left[i] = index - i - 1
            else:
                left[i] = l - i - 1
            stack.append((i, heights[i]))
        
        right[0] = 0
        stack = []
        for i in range(0, l):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if stack:
                index = stack[-1][0]
                right[i] = i - index - 1
            else:
                right[i] = i
            stack.append((i, heights[i]))
        
        maxArea = heights[0]
        for i in range(l):
            maxArea = max(maxArea, heights[i]*(left[i]+right[i]+1))
        
        print(left, right)
        return maxArea

        