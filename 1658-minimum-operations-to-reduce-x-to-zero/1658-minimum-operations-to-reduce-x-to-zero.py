class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        max_window_length = -1
        curr_sum_of_window = 0
        left = 0
        # Sliding Window approach
        for right in range(len(nums)):
            # Calculate the curr_sum of the window
            curr_sum_of_window += nums[right]
            
            # Case 1: If curr_sum is larger than target, increment left pointer by 1
            while left <= right and curr_sum_of_window > target:
                curr_sum_of_window -= nums[left]
                left += 1
            
            # Case 2: If curr_sum is actually equal to target, we update the max_window_length
            if curr_sum_of_window == target:
                max_window_length = max(max_window_length, right - left + 1)
        
        return -1 if max_window_length == -1 else len(nums) - max_window_length