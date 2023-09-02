class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        uniqueCombinations = []
        
        def findCombinations(index, currentCombination, currentTotal):
            if index >= len(candidates) or currentTotal > target:
                return
            if currentTotal == target:
                uniqueCombinations.append(currentCombination.copy())
                return
            
            currentCombination.append(candidates[index])
            findCombinations(index, currentCombination, candidates[index] + currentTotal)
            
            currentCombination.pop()
            findCombinations(index + 1, currentCombination, currentTotal)
            
        findCombinations(0, [], 0)
        return uniqueCombinations
        