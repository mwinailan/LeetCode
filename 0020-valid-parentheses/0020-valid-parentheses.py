class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisStack = []
        parenthesisMap = { ")" : "(", "]" : "[", "}" : "{"}
        
        for p in s:
            if p not in parenthesisMap:
                parenthesisStack.append(p)
                continue
            if not parenthesisStack or parenthesisStack[-1] != parenthesisMap[p]:
                return False
            parenthesisStack.pop()
        
        return not parenthesisStack