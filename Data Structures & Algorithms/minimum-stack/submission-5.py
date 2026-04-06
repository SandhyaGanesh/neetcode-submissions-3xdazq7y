import heapq
class MinStack:

    def __init__(self):
        self.minHeap = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        heapq.heappush(self.minHeap, val)

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1]

    def getMin(self) -> int:
        res = 0
        while self.minHeap: 
            res = self.minHeap[0]
            if res not in self.minStack:
                heapq.heappop(self.minHeap)
            else:
                break
        return res
