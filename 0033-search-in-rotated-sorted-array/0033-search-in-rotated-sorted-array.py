class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            # 4 5 6 7 0 1 2

            # left side
            if nums[0] <= nums[middle]:
                if target < nums[0] or target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1

            else:
                if target > nums[len(nums) - 1]  or target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
        return -1