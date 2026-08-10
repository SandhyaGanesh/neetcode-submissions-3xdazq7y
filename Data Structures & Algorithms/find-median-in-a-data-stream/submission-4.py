class MedianFinder:

    def __init__(self):
        self.count = 0
        self.firstHalf = []
        self.secondHalf = []

    def addNum(self, num: int) -> None:
        #print(self.firstHalf, self.secondHalf)
        if not self.firstHalf:
            heapq.heappush(self.firstHalf, -1 * num)
            return
        
        if num >= -1 * self.firstHalf[0]:
            heapq.heappush(self.secondHalf, num)
        else:
            heapq.heappush(self.firstHalf, -1 * num)
        
        if len(self.firstHalf) > len(self.secondHalf) + 1:
            heapq.heappush(self.secondHalf, -1 * heapq.heappop(self.firstHalf))
        elif len(self.secondHalf) > len(self.firstHalf) + 1:
            heapq.heappush(self.firstHalf, -1 * heapq.heappop(self.secondHalf))

    def findMedian(self) -> float:
        #print(self.firstHalf, self.secondHalf)
        if not self.firstHalf:
            return 0.0
        
        if (len(self.firstHalf) + len(self.secondHalf))%2 == 1:
            return float(-1 * self.firstHalf[0]) if len(self.firstHalf) > len(self.secondHalf) else self.secondHalf[0]
        else:
            return (-1.0 * self.firstHalf[0] + self.secondHalf[0])/2
        