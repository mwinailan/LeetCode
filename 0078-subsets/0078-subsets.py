class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsetResults = []
        currentSubset = []
        
        def findSubsets(currentSubset, index):
            if index >= len(nums):
                subsetResults.append(currentSubset.copy())
                return
                
            currentSubset.append(nums[index])
            findSubsets(currentSubset, index+1)
            
            currentSubset.pop()
            findSubsets(currentSubset, index+1)
    
        findSubsets(currentSubset, 0)
        return subsetResults
            
            
        