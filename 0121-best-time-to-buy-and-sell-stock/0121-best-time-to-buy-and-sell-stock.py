class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyTime = 0
        sellTime = 1
        
        while (sellTime < len(prices)):
            if prices[sellTime] > prices[buyTime]:
                profit = prices[sellTime] - prices[buyTime]
                maxProfit = max(profit, maxProfit)
            else:
                buyTime = sellTime
            sellTime += 1
        
        return maxProfit
        