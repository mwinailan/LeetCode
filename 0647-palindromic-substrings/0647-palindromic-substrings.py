class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # Loop through each character, and find odd and even length palindromes
        for i in range(len(s)):
            # Case 1: Odd-length palindrome counting
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            # Case 2: even-length palindrome counting
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            
        return res