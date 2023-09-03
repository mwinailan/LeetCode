class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberPair = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in numberPair:
                return [i, numberPair[difference]]
            numberPair[n] = i
        