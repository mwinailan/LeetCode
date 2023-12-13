class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sCharCount = Counter(s)
        #tCharCount = Counter(t)
        
        if len(s) != len(t):
            return False
        
        sCharCount = [0] * 26
        tCharCount = [0] * 26
        
        for i in range(len(s)):
            sCharCount[ord(s[i]) - ord("a")] += 1
            tCharCount[ord(t[i]) - ord("a")] += 1
        
        return sCharCount == tCharCount
        