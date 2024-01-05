class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap solution
        valueToIndex = {}
        
        # Iterate through nums to find the solution O(n)
        for i, num in enumerate(nums):
            difference = target - num
            if difference in valueToIndex:
                return [i, valueToIndex[difference]]
            
            valueToIndex[num] = i
                