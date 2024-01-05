class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for string in strs:
            letterCount = [0] * 26
            # Count the letters, and use the resulting list as a tuple for the key in hashmap
            for s in string:
                letterCount[ord(s) - ord("a")] += 1
            
            anagrams[tuple(letterCount)].append(string)
                
        
        return anagrams.values()
        