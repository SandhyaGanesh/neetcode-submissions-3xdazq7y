class Solution:
    def __init__(self):
        self.memo = {}
    def maxProfit(self, prices: List[int]) -> int:
        if tuple(prices) in self.memo:
            return self.memo[tuple(prices)]
        l = len(prices)
        maxProfit = 0
        i = 0
        while i < l:
            for j in range(i+1, l):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i] + self.maxProfit(prices[j+1:])
                    maxProfit = max(maxProfit, profit)
                else:
                    i = j - 1
                    break
            i += 1
        self.memo[tuple(prices)] = maxProfit
        return maxProfit