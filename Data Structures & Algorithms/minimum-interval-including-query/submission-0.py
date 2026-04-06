class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()

        heap = []
        heapq.heapify(heap)
        res = []
        s = 0
        e = 0
        for q, i in queries:
            while s < len(intervals) and intervals[s][0] <= q:
                heapq.heappush(heap, (intervals[s][1] - intervals[s][0] + 1, intervals[s][1]))
                s += 1
            print(heap)
            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            if not heap:
                res.append(-1)
            else:
                res.append(heap[0][0])
        newRes = [0]*len(queries)
        for i in range(len(queries)):
            newRes[queries[i][1]] = res[i]
        return newRes