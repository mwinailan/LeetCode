class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap solution
        resmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in resmap:
                return [resmap[diff], i]
            resmap[n] = i
        