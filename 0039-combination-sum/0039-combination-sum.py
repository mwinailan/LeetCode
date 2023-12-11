class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        # Backtracking solution using DFS, going through each candidate
        def findCombinations(i, currentCombination, totalSum):
            if totalSum == target:
                combinations.append(currentCombination.copy())
                return
            if totalSum > target or i >= len(candidates):
                return
            
            currentCombination.append(candidates[i])
            findCombinations(i, currentCombination, totalSum + candidates[i])
            currentCombination.pop()
            findCombinations(i + 1, currentCombination, totalSum)
            
        findCombinations(0, [], 0)
        return combinations
            