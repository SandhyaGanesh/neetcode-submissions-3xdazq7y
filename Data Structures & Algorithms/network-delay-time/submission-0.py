class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [-1 for _ in range(n)]
        adjList = {}
        for i in range(1, n+1):
            adjList[i] = []
        for src, dst, tim in times:
            adjList[src].append((tim, dst))
        
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            t, n = heapq.heappop(minHeap)
            print(t, n)
            if time[n-1] != -1 and time[n-1] <= t:
                continue
            time[n-1] = t
            for tim, neighbor in adjList[n]:
                heapq.heappush(minHeap, (t+tim, neighbor))
        
        print(time)
        if min(time) == -1:
            return -1
        else:
            return max(time)