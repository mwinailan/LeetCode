class Solution:
    def isHappy(self, n: int) -> bool:
        
        isPresent = set()
        
        while n:
            if n in isPresent:
                return False
            
            isPresent.add(n)
            
            n = self.calculateSquares(n)
            
            if n == 1:
                return True
        
        return False
        
    def calculateSquares(self, n):
        output = 0
        while n:
            rightMost = n % 10
            output += rightMost ** 2
            n = n // 10
        
        return output
            
        