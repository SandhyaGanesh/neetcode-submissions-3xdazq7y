class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = []
        currStart, currEnd = intervals[0][0], intervals[0][1]
        for interval in intervals:
            if interval[0] > currEnd:
                mergedIntervals.append([currStart, currEnd])
                currStart = interval[0] 
            currEnd = max(interval[1], currEnd)
        mergedIntervals.append([currStart, currEnd])    
        return mergedIntervals