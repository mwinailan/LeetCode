class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSubarray = nums[0]
        currentSubarray = 0
        
        for n in nums:
            currentSubarray += n
            maximumSubarray = max(maximumSubarray, currentSubarray)
            
            if currentSubarray < 0:
                currentSubarray = 0
            
        return maximumSubarray