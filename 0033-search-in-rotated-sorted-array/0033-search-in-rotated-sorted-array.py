class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # Binary search
        # O(logn) time complexity
        while ( left <= right ):
            middle = ( right + left )// 2
            if nums[middle] == target:
                return middle
            
            # Case 1 Search left sorted array
            if nums[middle] >= nums[0]:
                if nums[middle] < target or target < nums[0]:
                    left = middle + 1
                else:
                    right = middle - 1
                
            # Case 2 Search right sorted array
            else:            
                if nums[middle] > target or target > nums[-1]:
                    right = middle - 1
                else:
                    left = middle + 1
                    
        return -1