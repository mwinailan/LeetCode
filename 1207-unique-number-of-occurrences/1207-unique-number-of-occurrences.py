class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence_count_set = set()
        
        number_occurences = {}
        
        # 2 pass linear solution
        for n in arr:
            number_occurences[n] = 1 + number_occurences.get(n, 0)
        
        for count in number_occurences.values():
            if count in occurence_count_set:
                return False
            occurence_count_set.add(count)
        
        return True
        
        
        