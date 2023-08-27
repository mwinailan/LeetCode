class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValStack = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        
        if self.minValStack:
            self.minValStack.append(min(self.minValStack[-1], val))
        else:
            self.minValStack.append(val)
        
        

    def pop(self) -> None:
        self.minStack.pop()
        self.minValStack.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.minValStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()