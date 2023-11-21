class Solution:
    def climbStairs(self, n: int) -> int:
        oneDown, twoDown = 1, 2
        
        if n == 1:
            return oneDown
        if n == 2:
            return twoDown
        
        i = 0
        while i < (n - 2):
            temp = oneDown + twoDown
            oneDown = twoDown
            twoDown = temp
            i += 1
            
        return twoDown
            
        
        