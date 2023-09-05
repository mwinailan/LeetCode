class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solution = []
        currentSubsets = []
        nums.sort()
        
        def findSubsets(index, curentSubsets):
            if index == len(nums):
                solution.append(currentSubsets.copy())
                return
                
            currentSubsets.append(nums[index])
            findSubsets(index + 1, currentSubsets)
            currentSubsets.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            findSubsets(index + 1, currentSubsets)
            
        findSubsets(0, [])
        return solution