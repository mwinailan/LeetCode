class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesStack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        
        for symbol in s:
            if symbol in closeToOpen:
                if parenthesesStack and parenthesesStack[-1] == closeToOpen[symbol]:
                    parenthesesStack.pop()
                else:
                    return False
            else:
                parenthesesStack.append(symbol)
        
        if parenthesesStack:
            return False
        else:
            return True
            
        