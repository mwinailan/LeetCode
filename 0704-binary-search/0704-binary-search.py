class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search solution O(log n)
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Case 1: target value larger than nums[mid], search right side
            if target > nums[mid]:
                left = mid + 1
            # Case 2: target value smaller than nums[mid], search left side
            elif target < nums[mid]:
                right = mid - 1
            
            # Case 3: return mid if target == nums[mid]
            else:
                return mid
            
            
        # if value does not exist in nums
        return -1