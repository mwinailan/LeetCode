class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        parenthesisStack = []
        
        for c in s:
            # Case 1: c is a closing bracket
            if c in closeToOpen:
                # Case 1.1: c matches the top of parenthesisStack
                if parenthesisStack and parenthesisStack[-1] == closeToOpen[c]:
                    parenthesisStack.pop()
                # Case 1.2: c doesnt match
                else:
                    return False
            # Case 2: c is an opening bracket:
            else:
                parenthesisStack.append(c)
                
        return len(parenthesisStack) == 0
        