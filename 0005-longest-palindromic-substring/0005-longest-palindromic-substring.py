class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromeLength = 0
        currentSubstring = ""
        # Loop through every letter in s
        for i in range(len(s)):            
            # Look for odd length palindromes
            l, r = i, i
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if (r - l + 1) > longestPalindromeLength:
                    currentSubstring = s[l:r+1]
                    longestPalindromeLength = r - l + 1
                l -= 1
                r += 1
            
            # Look for even length palindromes
            l, r = i, i + 1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if (r - l + 1) > longestPalindromeLength:
                    currentSubstring = s[l:r+1]
                    longestPalindromeLength = r - l + 1
                l -= 1
                r += 1
    
        return currentSubstring