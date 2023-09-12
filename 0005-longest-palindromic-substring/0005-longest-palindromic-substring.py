class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstring = 0
        res = ""
        
        for i in range(len(s)):
            left, right = i, i
            while left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                longestSubstring = max(longestSubstring, right - left + 1)
                if (right - left + 1 == longestSubstring):
                    res = s[left:right + 1]
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                longestSubstring = max(longestSubstring, right - left + 1)
                if (right - left + 1 == longestSubstring):
                    res = s[left:right + 1]
                left -= 1
                right += 1
        
        
        return res
        