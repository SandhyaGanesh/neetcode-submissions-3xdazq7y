class Solution:
    def __init__(self):
        self.memo = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or amount < 0:
            return -1
        if (amount, tuple(coins)) in self.memo:
            return self.memo[(amount, tuple(coins))]
        
        coins.sort()
        highestDenomination = coins.pop()
        maxCoins = amount // highestDenomination
        res = []
        for i in range(0, maxCoins + 1):
            newAmount = amount - (i * highestDenomination)
            change = self.coinChange(coins.copy(), newAmount)
            if change != -1:
                res.append(i + change)
        coins.append(highestDenomination)
        self.memo[(amount, tuple(coins))] = min(res) if res else -1
        return self.memo[(amount, tuple(coins))]
