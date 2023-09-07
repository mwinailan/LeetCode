class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 1, 1
        maxProduct = max(nums)
        for num in nums:
            if num == 0:
                minProd, maxProd = 1, 1
                
            temp = maxProd
            maxProd = max(num * maxProd, num * minProd, num)
            minProd = min(num * temp, num * minProd, num)
            maxProduct = max(maxProduct, maxProd)
        
        return maxProduct
        