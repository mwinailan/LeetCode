class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in diff:
                return [i, diff[difference]]
            else:
                diff[n] = i
        