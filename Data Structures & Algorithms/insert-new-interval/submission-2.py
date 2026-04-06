class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = [[-float("inf"), -float("inf")]] + intervals + [[float("inf"), float("inf")]]
        for i in range(len(intervals) - 1):
            if intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]:
                intervals.insert(i+1, newInterval)
                return intervals[1:-1]
            elif intervals[i][0] < newInterval[0] and intervals[i][1] > newInterval[1]:
                return intervals[1:-1]
        
        startIndex = 0
        endIndex = len(intervals) - 1

        while startIndex < len(intervals):
            if intervals[startIndex][1] >= newInterval[0]:
                break
            startIndex += 1
        a = min(intervals[startIndex][0], newInterval[0])
        print(startIndex)
        while endIndex >= startIndex:
            if intervals[endIndex][0] <= newInterval[1]:
                break
            endIndex -= 1
        b = max(intervals[endIndex][1], newInterval[1])
        print(endIndex)
        for i in range(startIndex, endIndex + 1):
            intervals.pop(startIndex)
        intervals.insert(startIndex, [a,b])

        return intervals[1:-1]
            