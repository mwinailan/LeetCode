class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currentSubset = []
        def findSubsets(index):
            if index >= len(nums):
                subsets.append(currentSubset.copy())
                return
            
            currentSubset.append(nums[index])
            findSubsets(index + 1)
            
            currentSubset.pop()
            findSubsets(index + 1)
            
        findSubsets(0)
        return subsets
        