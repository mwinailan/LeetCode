class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, currentSubstring = [], []
        
        def findSubstrings(i):
            if i >= len(s):
                res.append(currentSubstring.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    currentSubstring.append(s[i:j+1])
                    findSubstrings(j + 1)
                    currentSubstring.pop()
        findSubstrings(0)
        return res
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True