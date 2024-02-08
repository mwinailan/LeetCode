class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToDiff = {}
        
        for i, n in enumerate(nums):
            diff =  target - n
            
            if diff in numsToDiff:
                return [i, numsToDiff[diff]]
            
            numsToDiff[n] = i
    
        