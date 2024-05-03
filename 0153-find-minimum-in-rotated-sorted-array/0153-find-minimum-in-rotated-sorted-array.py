class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = float("Inf")
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            middle = (left + right) // 2
            min_value = min(min_value, nums[middle])
            
            # right has the minimum value
            if nums[middle] > nums[right]:
                left = middle + 1
            # left has the minimum value
            else:
                right = middle - 1
                
        return min(min_value, nums[0])
        