class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphanumeric(l: chr):
            if (ord(l) >= ord('A') and ord(l) <= ord('Z') or ord(l) >= ord('a') and ord(l) <= ord('z') or ord(l) >= ord('0') and ord(l) <= ord('9')):
                return True
            else:
                return False

        left = 0
        right = len(s) - 1

        while(left < right):
            while (isAlphanumeric(s[left]) is False and left < right):
                left = left + 1
            
            while (isAlphanumeric(s[right]) is False and left < right):
                right = right - 1

            if (s[left].lower() != s[right].lower()):
                return False
            
            left = left + 1
            right = right - 1
            
        return True