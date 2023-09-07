class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsNeededForAmount = [(amount + 1)] * (amount + 1)
        coinsNeededForAmount[0] = 0
        
        for amount in range(1, amount + 1):
            for coin in coins:
                if (amount - coin) >= 0:
                    coinsNeededForAmount[amount] = min(coinsNeededForAmount[amount], 1 + coinsNeededForAmount[amount - coin])
        
        
        if coinsNeededForAmount[amount] == (amount + 1):
            return -1
        else:
            return coinsNeededForAmount[amount]
        