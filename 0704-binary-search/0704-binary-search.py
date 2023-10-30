class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search
        # initialize left and right pointer
        left, right = 0, len(nums) - 1
        
        # criteria left <= right
        while left <= right:
            # find middle point
            middle = left + (right - left) // 2
            # use mid point to find target
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        # still couldnt find answer
        return -1
        