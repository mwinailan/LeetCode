class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(c):
            if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                return True
            else:
                return False
        
        # 2 pointer solution, 1 pass O(n)
        left, right = 0, len(s)-1
        
        while(left < right):
            # Remove non alphanumeric
            while not isAlphaNumeric(s[left]) and left < right:
                left += 1
            while not isAlphaNumeric(s[right]) and left < right:
                right -= 1 
            
            # Compare 
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True