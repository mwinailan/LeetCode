class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        isContained = set()
        longestSubstringLength = 0
        
        # O(n) solution 
        for right in range(len(s)):
            # while the letter is in the set, we remove it
            while s[right] in isContained:
                isContained.remove(s[left])
                left += 1
            
            # Add current letter to the set
            isContained.add(s[right])
            
            # calculate current length and compare to the longest
            longestSubstringLength = max(longestSubstringLength, right - left + 1)
        
        
        return longestSubstringLength
        