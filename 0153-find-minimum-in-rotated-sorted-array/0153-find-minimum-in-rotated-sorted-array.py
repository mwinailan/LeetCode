class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                minVal = min(minVal, nums[left])
                break
            
            middle = (left + right) // 2
            minVal = min(minVal, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return minVal
        