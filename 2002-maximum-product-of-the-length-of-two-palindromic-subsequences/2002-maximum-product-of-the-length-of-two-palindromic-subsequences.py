class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        palindrome = {}
        res = 0
        
        for mask in range(1, 2 ** N):
            substr = ""
            for i in range(N):
                if mask & (1 << i):
                    substr += s[i]
            
            if substr == substr[::-1]:
                palindrome[mask] = len(substr)
        
        
        for m1 in palindrome:
            for m2 in palindrome:
                if m1 & m2 == 0:
                    res = max(res, palindrome[m1] * palindrome[m2])
        
        return res