class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToLetters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
         }
        
        def findCombinations(i, currentRes):
            if len(currentRes) == len(digits):
                res.append(currentRes)
                return
            
            
            for l in digitToLetters[digits[i]]:
                findCombinations(i+1, currentRes + l)
        
        if digits:
            findCombinations(0,"")
        
        return res
        