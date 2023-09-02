class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        pointer = 0
        currentSum = 0
        while pointer < len(nums):
            currentSum += nums[pointer]
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
            pointer += 1
        
        return maxSum
        