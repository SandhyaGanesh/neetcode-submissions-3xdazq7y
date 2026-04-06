class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and -num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                n = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, n)
            else:
                n = -1 * heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, n)
        
    def findMedian(self) -> float:
        if abs(len(self.maxHeap) - len(self.minHeap)) == 1:
            if len(self.maxHeap) > len(self.minHeap):
                return -1.0 * self.maxHeap[0]
            else:
                return 1.0 * self.minHeap[0]
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0] ) / 2