class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        
        for right in range(1, len(prices)):
            #Case 1: if prices in right is larger than prices in left, then we find the max profit available
            if prices[right] >= prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            #Case 2: if prices in right is smaller than prices in left, then we shift left to right price
            elif prices[right] < prices[left]:
                left = right
        
        return maxProfit
