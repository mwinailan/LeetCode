class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        left, right = 0, len(nums) - 1
        
        4, 3, 2, 3, 4
        while(left < right):
            if nums[left] > nums[right]:
                nums[right] += nums[right - 1]
                del nums[right - 1]
                operations += 1
            elif nums[left] < nums[right]:
                nums[left] += nums[left + 1]
                del nums[left + 1]
                operations += 1
            else:
                left += 1
            right -= 1
        
        return operations
        