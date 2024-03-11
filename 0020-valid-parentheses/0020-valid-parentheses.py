class Solution:
    def isValid(self, s: str) -> bool:
        closingToOpening = {")" : "(", "]" : '[', "}" : "{"}
        parenthesesStack = []
        
        for c in s:
            # Case 1: Closed brackets
            if c in closingToOpening and parenthesesStack:
                curr = parenthesesStack.pop()
                if closingToOpening[c] != curr:
                    return False
            # Case 2: Opening Brackets
            else:
                parenthesesStack.append(c)
        
        return len(parenthesesStack) == 0