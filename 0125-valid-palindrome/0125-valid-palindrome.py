class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        def isAlphaNumeric(c):
            if (ord(c) <= ord("z") and ord(c) >= ord("a")) or (ord(c) <= ord("9") and ord(c) >= ord("0")):
                return True
            else:
                return False
            
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        # 2 Pointer Solution
        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left += 1
            while left < right and not isAlphaNumeric(s[right]):
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
            
        