class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search method
        left, right = 0, len(nums) - 1
        minimumElement = nums[0]
        while (left<=right):
            if nums[left] < nums[right]:
                minimumElement = min(minimumElement, nums[left])
                break
                
            
            middle = (left + right) // 2
            minimumElement = min(minimumElement, nums[middle])
            
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return minimumElement
        