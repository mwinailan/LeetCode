class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        lengthLongest = 0
        left = 0
        letterCount = {}
        for r in range(len(s)):
            letterCount[s[r]] = 1 + letterCount.get(s[r], 0)
            while (r - left + 1) - max(letterCount.values()) > k:
                letterCount[s[left]] = letterCount[s[left]] - 1
                left += 1
            lengthLongest = max(lengthLongest, r - left + 1)
        
        return lengthLongest