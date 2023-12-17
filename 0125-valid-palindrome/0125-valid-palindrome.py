class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphanumeric(l: chr):
            if (ord(l) >= ord('A') and ord(l) <= ord('Z') or ord(l) >= ord('a') and ord(l) <= ord('z') or ord(l) >= ord('0') and ord(l) <= ord('9')):
                return True
            else:
                return False
            
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        while (left < right):
            # Move pointers until we find alphanumeric
            while left < right and not isAlphanumeric(s[left]):
                left += 1
            while left < right and not isAlphanumeric(s[right]):
                right -= 1
                
            # Compare both left and right pointers, then move them by 1
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True