from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        dp = [0, 0, 0]
        for c in costs:
            dp0 = c[0] + min(dp[1], dp[2])
            dp1 = c[1] + min(dp[0], dp[2])
            dp2 = c[2] + min(dp[1], dp[0])
            dp = [dp0, dp1, dp2]

        return min(dp)
