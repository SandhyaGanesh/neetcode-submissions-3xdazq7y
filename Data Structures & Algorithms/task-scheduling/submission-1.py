class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreqMap = {}
        for task in tasks:
            taskFreqMap[task] = taskFreqMap.get(task, 0) + 1
        taskHeap = []
        for task, freq in taskFreqMap.items():
            heapq.heappush(taskHeap, (-1 * freq, task))
        
        clock = 0
        q = deque()
        while q or taskHeap:
            clock += 1

            if not taskHeap:
                clock = q[0][1]
            else:
                f, t = heapq.heappop(taskHeap)
                f += 1
                if f < 0:
                    q.append((f, clock + n, t))
            if q and q[0][1] <= clock:
                f, c, t = q.popleft()
                heapq.heappush(taskHeap, (f, t))
        
        return clock

        
        return clock

