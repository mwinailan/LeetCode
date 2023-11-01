class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic programming
        lengthOfLIS = [1] * len(nums)
        
        # Start from the end (len(nums)) and iterate to the start
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if (nums[i] < nums[j]):
                    # Calculate the LIS at index i
                    lengthOfLIS[i] = max(lengthOfLIS[i], 1 + lengthOfLIS[j])
        
        return max(lengthOfLIS)