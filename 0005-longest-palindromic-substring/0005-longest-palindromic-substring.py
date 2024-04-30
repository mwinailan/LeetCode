class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        longest_palindromic_substring = ""
        for i in range(len(s)):
            left, right = i, i
            current_substring = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_substring = s[left:right + 1]
                left -= 1
                right += 1
            
            if len(current_substring) > len(longest_palindromic_substring):
                longest_palindromic_substring = current_substring
            
            left, right = i, i + 1
            current_substring = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_substring = s[left:right + 1]
                left -= 1
                right += 1
            
            if len(current_substring) > len(longest_palindromic_substring):
                longest_palindromic_substring = current_substring
            
        return longest_palindromic_substring