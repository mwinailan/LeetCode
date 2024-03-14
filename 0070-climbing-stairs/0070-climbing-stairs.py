class Solution:
    def climbStairs(self, n: int) -> int:
        oneBelow = 1
        twoBelow = 1
        
        for i in range(n - 1):
            temp = oneBelow
            oneBelow = oneBelow + twoBelow
            twoBelow = temp
        
        return oneBelow