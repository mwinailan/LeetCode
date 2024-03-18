class Solution:
    def partitionString(self, s: str) -> int:
        number_of_partitions = 0
        seen_letters = set()
        
        for c in s:
            if c in seen_letters:
                number_of_partitions += 1
                seen_letters = set()
            
            seen_letters.add(c)
        
        if len(seen_letters) > 0:
            number_of_partitions += 1
        
        return number_of_partitions
        
        