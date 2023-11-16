class Solution:
    def wordPattern(self, pattern, s) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for char, word in zip(pattern, words):
            if (char in charToWord and charToWord[char] != word) or (word in wordToChar and wordToChar[word] != char):
                return False
            
            charToWord[char] = word
            wordToChar[word] = char
        
        return True