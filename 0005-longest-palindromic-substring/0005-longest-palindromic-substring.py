class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromicSubstring = ""
        # O(n^2) time complexity
        for i in range(len(s)):
            # Find the odd length palindrome
            left, right = i, i
            while left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                if (right - left + 1) > len(longestPalindromicSubstring):
                    longestPalindromicSubstring = s[left:right + 1]
                left -= 1
                right += 1 
            
            # Find the even length palindrome
            left, right = i, i + 1
            while left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                if (right - left + 1) > len(longestPalindromicSubstring):
                    longestPalindromicSubstring = s[left:right + 1]
                left -= 1
                right += 1 
            
        return longestPalindromicSubstring
            
        