class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisStack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}
        
        for p in s:
            if p in ["(", "[", "{"]:
                parenthesisStack.append(p)
            
            else:
                if parenthesisStack and parenthesisStack[-1] == closeToOpen[p]:
                    parenthesisStack.pop()
                else:
                    return False
        
        return True if len(parenthesisStack) == 0 else False