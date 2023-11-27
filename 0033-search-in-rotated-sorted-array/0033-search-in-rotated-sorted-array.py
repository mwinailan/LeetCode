class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search soluition for O(nlogn) runtime
        left, right = 0, len(nums) - 1
        
        while(left <= right):
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            # Case 1: If mid is in the left sorted portion
            elif nums[mid] >= nums[0]:
                # Case 1.1:
                if target > nums[mid] or target < nums[0]:
                    left = mid + 1
                # Case 1.2:
                else: 
                    right = mid - 1
                
            # Case 2: If mid is in the right sorted portion
            else:
                # Case 2.1:
                if target < nums[mid] or target > nums[len(nums) - 1]:
                    right = mid - 1
                # Case 2.2:
                else:
                    left = mid + 1
            
        return -1