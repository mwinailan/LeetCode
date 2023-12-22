class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        
        for right in range(len(prices)):
            # Case 1: If prices[right] is lower than prices[left], move the left pointer to right
            if prices[right] < prices[left]:
                left = right
            # Case 2: If prices[left] is lower than prices[right], compute currentProfit, and move the right pointer
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
        
        return maxProfit
                