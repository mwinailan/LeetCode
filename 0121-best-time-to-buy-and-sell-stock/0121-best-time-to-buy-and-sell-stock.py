class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer solution
        buy = 0
        max_profit = 0
        
        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            
            max_profit = max(max_profit, prices[sell] - prices[buy])
        
        return max_profit