class Solution:
    def __init__(self):
        self.memo = {}
    
    def change(self, amount: int, coins: List[int]) -> int:
        if (amount, tuple(coins)) in self.memo:
            return self.memo[(amount, tuple(coins))]
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if not coins:
            return 0

        include = self.change(amount - coins[0], coins)
        exclude = self.change(amount, coins[1:])
        self.memo[(amount, tuple(coins))] = include + exclude
        return include + exclude