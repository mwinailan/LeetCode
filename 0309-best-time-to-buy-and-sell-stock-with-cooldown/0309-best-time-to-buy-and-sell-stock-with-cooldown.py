class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitAtIndex = {}
        
        def findMaxProfit(index, buying):
            if index >= len(prices):
                return 0
            if (index, buying) in maxProfitAtIndex:
                return maxProfitAtIndex[(index, buying)]
            
            if buying:
                buy = findMaxProfit(index + 1, False) - prices[index]
                cooldown = findMaxProfit(index + 1, True)
                maxProfitAtIndex[(index,buying)] = max(buy, cooldown)
            else:
                sell = findMaxProfit(index + 2, True) + prices[index]
                cooldown = findMaxProfit(index + 1, False)
                maxProfitAtIndex[(index,buying)] = max(sell, cooldown)
            
            return maxProfitAtIndex[(index,buying)]
        
        return findMaxProfit(0, True)
        