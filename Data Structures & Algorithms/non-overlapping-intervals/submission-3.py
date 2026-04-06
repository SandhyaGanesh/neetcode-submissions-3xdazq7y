class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        intervalsRemoved = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd:
                intervalsRemoved += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return intervalsRemoved