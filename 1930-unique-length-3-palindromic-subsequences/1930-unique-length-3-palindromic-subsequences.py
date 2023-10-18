class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        leftPortion = set()
        rightPortion = collections.Counter(s)
        
        for i in range(len(s)):
            rightPortion[s[i]] -= 1
            if rightPortion[s[i]] == 0:
                rightPortion.pop(s[i])
            
            for j in range(26):
                char = chr(ord("a") + j)
                if char in leftPortion and char in rightPortion:
                    res.add((s[i], char))
            
            leftPortion.add(s[i])
            
        return len(res)