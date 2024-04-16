class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        current_sum = 0
        
        for n in nums:
            current_sum += n
            largest_sum = max(largest_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        
        return largest_sum