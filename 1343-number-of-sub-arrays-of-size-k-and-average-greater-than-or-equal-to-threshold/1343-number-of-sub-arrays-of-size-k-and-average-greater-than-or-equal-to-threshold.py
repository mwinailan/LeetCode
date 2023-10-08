class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = sum(arr[:k-1])
        res = 0
        
        for l in range(len(arr) - k + 1):
            currSum += arr[l + k - 1] 
            avg = currSum / k
            if avg >= threshold:
                res += 1
            currSum -= arr[l]

        return res
        