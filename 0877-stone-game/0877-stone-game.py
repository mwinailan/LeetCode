class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # caching based on left and right pointers
        dp = {} # key = (l,r)
        def aliceStones(left, right):
            # Stopping criteria
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left,right)]
            
            # Determine whether it is alice's turn to take a stone
            leftPile = 0 if (len(piles) % 2) != 0 else piles[left]
            rightPile = 0 if (len(piles) % 2) != 0 else piles[right]
                
            # Find the maximum that alice can get from the left and right stone pile
            # Case 1: Alice takes the left pile
            # Case 2: Alice takes the right pile
            dp[(left,right)] = max(piles[left] + aliceStones(left + 1, right), piles[right] + aliceStones(left, right - 1))
        
            return dp[(left,right)]
        
        
        return aliceStones(0, len(piles) - 1) > sum(piles) // 2
            
            
        