class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMin = 1
        currentMax = 1
        maxProduct = max(nums)
        
        for n in nums:
            if n == 0:
                currentMin = 1
                currentMax = 1
                
            temp = n * currentMax
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(temp, n * currentMin, n)
            maxProduct = max(maxProduct, currentMax)
            
        return maxProduct
            
            