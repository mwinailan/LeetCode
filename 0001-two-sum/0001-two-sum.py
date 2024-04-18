class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in visited_nums:
                return [i, visited_nums[difference]]
            visited_nums[n] = i
        