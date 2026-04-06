class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        res = 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            res = max(res, price - minSoFar)
        return res