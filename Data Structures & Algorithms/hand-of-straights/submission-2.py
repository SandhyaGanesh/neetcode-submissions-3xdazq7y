class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        if l % groupSize != 0:
            return False
        
        heap = []
        for num in hand:
            heapq.heappush(heap, num)
        
        for i in range(l//groupSize):
            newHeap = []
            popped = heapq.heappop(heap)
            end = popped + groupSize - 1
            hand = []
            hand.append(popped)
            print("pass ", i, ": ", popped, heap, end)
            while hand[-1] < end:
                if not heap:
                    print("hey", hand)
                    return False
                
                popped = heapq.heappop(heap)
                if popped == hand[-1] + 1:
                    hand.append(popped)
                    continue
                elif popped == hand[-1]:
                    heapq.heappush(newHeap, popped)
                else:
                    print(hand)
                    return False
            print(heap, newHeap)
            for _ in range(len(heap)):
                popped = heapq.heappop(heap)
                heapq.heappush(newHeap, popped)
            heap = newHeap
            
        return True
