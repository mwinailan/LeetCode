class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currString = ""
        
        for c in path + "/":
            if c == "/":
                if currString == "..":
                    if stack: stack.pop()
                elif currString != "" and currString != ".":
                    stack.append(currString)
                currString = ""
                    
            else:
                currString += c
        
        return "/" + "/".join(stack)
    