class Solution:
    def minimizedStringLength(self, s: str) -> int:
        unique_strings = set()
        for c in s:
            unique_strings.add(c)
        
        return len(unique_strings)
            