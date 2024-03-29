class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        left, right = 0, len(nums) - 1
        
        #O(n) 2 pointer solution
        #O(1) memory usage
        while(left < right):
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            else:
                if nums[left] + nums[left + 1] < nums[right] + nums[right - 1]:
                    nums[left + 1] += nums[left]
                    left += 1
                else:
                    nums[right - 1] += nums[right]
                    right -= 1
                operations += 1
                    
        
        return operations
        