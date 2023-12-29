class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 1 , 1
        res = max(nums)
        for n in nums:
            temp = maxProd
            maxProd = max(maxProd * n, minProd * n, n)
            minProd = min(temp * n, minProd * n, n)
            res = max(maxProd, res)
        
        return res
            
        
        
            
        