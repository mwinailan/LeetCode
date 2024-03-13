class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # O(n) time complexity
        # O(n) space complexity
        sCounter = {}
        tCounter = {}
        
        for i in range(len(s)):
            sCounter[s[i]] = 1 + sCounter.get(s[i], 0)
            tCounter[t[i]] = 1 + tCounter.get(t[i], 0)
        
        return sCounter == tCounter
        
        