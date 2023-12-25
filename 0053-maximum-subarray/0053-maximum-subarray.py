class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray = nums[0]
        currSubarray = 0
        
        for n in nums:
            currSubarray += n
            maxSubarray = max(maxSubarray, currSubarray)
            
            if currSubarray < 0:
                currSubarray = 0
        
        return maxSubarray
        