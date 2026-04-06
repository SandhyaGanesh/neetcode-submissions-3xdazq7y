class Solution:
    def __init__(self):
        self.memo = {}

    def maxProfit(self, prices: List[int], startIdx = 0, bought = False) -> int:
        if startIdx >= len(prices):
            return 0
        
        if (startIdx, bought) in self.memo:
            return self.memo[(startIdx, bought)]
        
        res = self.maxProfit(prices, startIdx+1, bought)
        if bought:
            res = max(res, prices[startIdx] + self.maxProfit(prices, startIdx + 2, False))
        else:
            res = max(res, -prices[startIdx] + self.maxProfit(prices, startIdx + 1, True))
        
        self.memo[(startIdx, bought)] = res
        if startIdx == 0:
            print(self.memo)
        return res