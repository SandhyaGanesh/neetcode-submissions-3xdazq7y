class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h1 = nums
        heapq.heapify(self.h1)
        while len(self.h1) > k:
            heapq.heappop(self.h1)

    def add(self, val: int) -> int:
        heapq.heappush(self.h1, val)
        if len(self.h1) > self.k:
            heapq.heappop(self.h1)
        return self.h1[0]
