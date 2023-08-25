class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        parenthesesStack = []
        closeToOpen = {"}" : "{", ")" : "(", "]" : "["}
        
        for symbol in s:
            if symbol in closeToOpen:
                if parenthesesStack and parenthesesStack[-1]  == closeToOpen[symbol]:
                    parenthesesStack.pop()
                else:
                    return False
            else:
                parenthesesStack.append(symbol)
        
        if len(parenthesesStack) > 0:
            return False 
        else:
            return True
        