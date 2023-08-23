class Solution:
    def climbStairs(self, n: int) -> int:
        oneStepUp, twoStepUp = 1, 1
        for i in range(n-1):
            temp = oneStepUp
            oneStepUp += twoStepUp
            twoStepUp = temp
        
        return oneStepUp
        
        