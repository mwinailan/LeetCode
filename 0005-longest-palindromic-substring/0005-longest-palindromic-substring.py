class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubstring = 0
        res = ""
        
        # Iterate through every element, then find odd and even length palindromes
        for i in range(len(s)):
            # Find Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longestSubstring:
                    longestSubstring = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1
            
            # Find Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longestSubstring:
                    longestSubstring = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res