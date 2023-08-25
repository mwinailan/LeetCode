class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedStrings = defaultdict(list)
        for s in strs:
            countOfLetters = [0] * 26
            
            for c in s:
                countOfLetters[ord(c) - ord("a")] += 1
            
            groupedStrings[tuple(countOfLetters)].append(s)
        
        return groupedStrings.values()
                
        
        