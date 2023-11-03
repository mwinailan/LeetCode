class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        letterCountS = {}
        letterCountT = {}

        for letter in s:
            letterCountS[letter] = 1 + letterCountS.get(letter, 0)
        
        for letter in t:
            letterCountT[letter] = 1 + letterCountT.get(letter, 0)

        if (letterCountS == letterCountT):
            return True
        else:
            return False

    
        