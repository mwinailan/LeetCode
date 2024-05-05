class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contained_letters = set()
        longest_substring_without_repeating = 0
        
        left = 0
        for right in range(len(s)):
            while s[right] in contained_letters:
                contained_letters.remove(s[left])
                left += 1
            
            contained_letters.add(s[right])
            longest_substring_without_repeating = max(longest_substring_without_repeating, right - left + 1)
            
        return longest_substring_without_repeating