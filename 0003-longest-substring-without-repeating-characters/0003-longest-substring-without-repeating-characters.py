class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charInSubstring = set()
        maxLength = currentLength = left = 0
        
        for c in s:
            while c in charInSubstring:
                charInSubstring.remove(s[left])
                currentLength -= 1
                left += 1
            
            charInSubstring.add(c)
            currentLength += 1
            maxLength = max(maxLength, currentLength)
        
        return maxLength
        