class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and not word2:
            return ""
        if not word1:
            return word2
        if not word2:
            return word1
        
        combinedWord = ""
        
        wordPointer = 0
        
        while(wordPointer < len(word1) and wordPointer < len(word2)):
            combinedWord += word1[wordPointer]
            combinedWord += word2[wordPointer]
            wordPointer += 1
        
        while(wordPointer < len(word1)):
            combinedWord += word1[wordPointer]
            wordPointer += 1
        
        while(wordPointer < len(word2)):
            combinedWord += word2[wordPointer]
            wordPointer += 1
        
        return combinedWord
        