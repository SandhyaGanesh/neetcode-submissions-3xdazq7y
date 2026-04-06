class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intTuples = [tuple(interval) for interval in intervals]
        intTuples.sort()
        res = []
        print(intTuples)
        currentStart = intTuples[0][0]
        currentEnd = intTuples[0][1]
        for s, e in intTuples:
            if s > currentEnd:
                res.append([currentStart, currentEnd])
                currentStart = s
            currentEnd = max(e, currentEnd)
        res.append([currentStart, currentEnd])
        return res