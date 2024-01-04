class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray = nums[0]
        currentSubarray = 0
        
        for n in nums:
            # Update current
            currentSubarray += n
            
            # Update maxSubarray value
            maxSubarray = max(maxSubarray, currentSubarray)
            
            # Discard current sum if less than 0
            if currentSubarray < 0:
                currentSubarray = 0
            
        
        return maxSubarray
        