class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        currentParenthesis = []
        def generateUniqueParenthesis(openN, closeN, currentParenthesis):
            if closeN == openN == n:
                result.append("".join(currentParenthesis))
            
            if openN < n:
                currentParenthesis.append("(")
                generateUniqueParenthesis(openN + 1, closeN, currentParenthesis)
                currentParenthesis.pop()
            
            if closeN < openN:
                currentParenthesis.append(")")
                generateUniqueParenthesis(openN, closeN + 1, currentParenthesis)
                currentParenthesis.pop()
        
        generateUniqueParenthesis(0, 0, currentParenthesis)
        return result
        