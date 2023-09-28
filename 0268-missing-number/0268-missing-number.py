class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = -1 * len(nums)
        
        for i in range(len(nums)):
            res += (nums[i] - i)
        
        return abs(res)
    
    

        