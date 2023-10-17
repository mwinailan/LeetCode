class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = -1
        res = []
        for i in range(len(arr) - 1, -1, -1):
            res.append(maxSoFar)
            maxSoFar = max(maxSoFar, arr[i])
        
        return res[::-1]