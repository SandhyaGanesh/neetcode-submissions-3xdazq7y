class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = {}
        for task in tasks:
            taskFreq[task] = taskFreq.get(task, 0) + 1
        
        heap = []
        coolHeap = []
        for task in taskFreq:
            heapq.heappush(heap, (-1 * taskFreq[task], task))

        t = 1
        while (heap or coolHeap):
            if coolHeap and coolHeap[0][1] == t:
                f, time, task = heapq.heappop(coolHeap)
                heapq.heappush(heap, (f, task))
            if heap:
                f, task = heapq.heappop(heap)
                f += 1
                time = t + n + 1
                if f != 0:
                    heapq.heappush(coolHeap, (f, time, task))
                t += 1
            else:
                t = coolHeap[0][1]
        return t - 1