class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {")" : "(", "]" : "[", "}" : "{"}
        parenthesis_stack = []
        
        for c in s:
            # Case 1: closing parenthesis
            if (parenthesis_stack and c in closing_to_opening):
                current_parenthesis = parenthesis_stack.pop()
                if current_parenthesis != closing_to_opening[c]:
                    return False
                    
            # Case 2: opening parenthesis
            else:
                parenthesis_stack.append(c)
        
        return len(parenthesis_stack) == 0