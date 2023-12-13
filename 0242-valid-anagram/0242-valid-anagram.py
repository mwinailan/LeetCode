class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharCount = Counter(s)
        tCharCount = Counter(t)
        
        return sCharCount == tCharCount
        