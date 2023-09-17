class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def findCombinations(index, currCombination, total):
            if total == target:
                res.append(currCombination.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            currCombination.append(candidates[index])
            findCombinations(index + 1, currCombination, total + candidates[index])
            currCombination.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            findCombinations(index + 1, currCombination, total)
            
        findCombinations(0, [], 0)
        return res
        