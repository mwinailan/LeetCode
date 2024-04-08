class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = {}
        for n in arr:
            num_count[n] = 1 + num_count.get(n, 0)
        
        num_set = set()
        for count in num_count.values():
            if count in num_set:
                return False
            num_set.add(count)
        
        return True