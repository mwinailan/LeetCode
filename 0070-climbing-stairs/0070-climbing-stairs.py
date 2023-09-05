class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        if n == 1:
            return first
        if n == 2:
            return second
        
        for i in range(2, n):
            temp = second
            second = first + second
            first = temp
        
        return second
        