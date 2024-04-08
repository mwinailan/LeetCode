class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = {}
        for n in arr:
            num_count[n] = 1 + num_count.get(n, 0)
        
        num_set = set()
        for num in num_count.keys():
            if num_count[num] in num_set:
                return False
            num_set.add(num_count[num])
        
        return True