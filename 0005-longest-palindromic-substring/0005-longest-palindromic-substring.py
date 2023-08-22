class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstringLength = 0
        longestPalindromeSubstring = ""
        
        for i in range(len(s)):
            left, right = i, i
            
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > longestSubstringLength):
                    longestPalindromeSubstring = s[left:right+1]
                    longestSubstringLength = right - left + 1
                right += 1
                left -= 1
                
        for i in range(len(s)):
            left, right = i, i + 1
            
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if (right - left + 1 > longestSubstringLength):
                    longestPalindromeSubstring = s[left:right+1]
                    longestSubstringLength = right - left + 1
                right += 1
                left -= 1
                
            
        
        return longestPalindromeSubstring
                