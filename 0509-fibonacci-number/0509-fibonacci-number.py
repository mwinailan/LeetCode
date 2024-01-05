class Solution:
    def fib(self, n: int) -> int:
        fibonacciRes = {}
        fibonacciRes[0] = 0
        fibonacciRes[1] = 1
        
        for i in range(2, n + 1):
            fibonacciRes[i] = fibonacciRes[i-1] + fibonacciRes[i-2]
        
        return fibonacciRes[n]