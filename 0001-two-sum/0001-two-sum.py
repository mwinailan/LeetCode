class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumbers = {}
        # O(n) memory and time
        for i, n in enumerate(nums):
            difference = target - n
            if difference in seenNumbers:
                return [i, seenNumbers[difference]]
            seenNumbers[n] = i
        
                
        