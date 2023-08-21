class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedNumbers = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            if (difference in visitedNumbers):
                return [i, visitedNumbers[difference]]
            visitedNumbers[num] = i