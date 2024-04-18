class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        
        for string in strs:
            letter_count = [0] * 26
            for c in string:
                letter_count[ord(c) - ord("a")] += 1
            
            group_anagrams[tuple(letter_count)].append(string)
        
        return group_anagrams.values()
        