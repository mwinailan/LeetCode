class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisStack = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}
        
        for c in s:
            # Case 1: c is a closing bracket
            if c in closeToOpen and parenthesisStack:
                current = parenthesisStack.pop()
                if current != closeToOpen[c]:
                    return False
            # Case 2: c is an opening bracket
            else:
                parenthesisStack.append(c)
        
        return len(parenthesisStack) == 0