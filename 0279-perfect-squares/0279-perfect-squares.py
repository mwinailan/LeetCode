class Solution:
    def numSquares(self, n) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s ** 2
                if target - square < 0:
                    break
                # if dp[target] < 1 + dp[n - square]:
                #     dp[target] = 1 + dp[n - square]
                dp[target] = min(dp[target], 1 + dp[target - square])
                    
        return dp[n]
        