class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        longestLength = 0
        for n in nums:
            currentLength = 0
            if (n - 1) not in numberSet:
                while (n + currentLength) in numberSet:
                    currentLength += 1
            
            longestLength = max(longestLength, currentLength)
        
        return longestLength