class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        is_contained = set()
        maxSum, currentSum = 0, 0
        # 2 pointer solution
        left = 0
        for right in range(len(nums)):
            while nums[right] in is_contained or right - left + 1 > k:
                is_contained.remove(nums[left])
                currentSum -= nums[left]
                left += 1
                
            is_contained.add(nums[right])
            currentSum += nums[right]
            
            if right - left + 1 == k:
                maxSum = max(maxSum, currentSum)
        
        return maxSum
        