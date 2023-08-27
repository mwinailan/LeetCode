class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for t in tokens:
            if t == "+":
                evalStack.append(evalStack.pop() + evalStack.pop())
            elif t == "*":
                evalStack.append(evalStack.pop() * evalStack.pop())
            elif t == "-":
                firstT = evalStack.pop()
                secondT = evalStack.pop()
                evalStack.append(secondT - firstT)
            elif t == "/":
                firstT = evalStack.pop()
                secondT = evalStack.pop()
                evalStack.append(int(secondT / firstT))
            else:
                evalStack.append(int(t))
            
        return evalStack[0]
                