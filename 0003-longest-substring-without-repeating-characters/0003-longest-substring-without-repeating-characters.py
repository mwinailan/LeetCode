class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 2 pointer solution to find substring window
        left = 0
        longestSubstring = 0
        isContained = set()
        for right in range(len(s)):
            while s[right] in isContained:
                isContained.remove(s[left])
                left += 1
            isContained.add(s[right])
            longestSubstring = max(longestSubstring, right - left + 1)
        
        return longestSubstring
        