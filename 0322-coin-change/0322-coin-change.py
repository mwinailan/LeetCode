class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinMemoization = [float("Inf")] * (amount + 1)
        coinMemoization[0] = 0
        
        for i in range(1, len(coinMemoization)):
            for c in coins:
                if (i - c) >= 0:
                    coinMemoization[i] = min(coinMemoization[i], 1 + coinMemoization[i-c])
                    
        return coinMemoization[amount] if coinMemoization[amount] != float("Inf") else -1
            