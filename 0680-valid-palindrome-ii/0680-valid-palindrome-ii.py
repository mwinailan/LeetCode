class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(s, canDelete):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r] and canDelete:
                    res = isPalindrome(s[l + 1:r + 1], False) or isPalindrome(s[l : r], False)
                    return res
                elif s[l] != s[r] and not canDelete:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        return isPalindrome(s, True)
        