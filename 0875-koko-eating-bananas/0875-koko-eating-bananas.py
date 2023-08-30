class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        low, high = 1, max(piles)
        
        
        # O(nLogn)
        while(low <= high):
            mid = (low + high) // 2
            eatTime = 0
            for bananas in piles:
                eatTime += math.ceil(bananas/mid)
            if eatTime > h:
                low = mid + 1
            else:
                high = mid - 1
                k = min(k, mid)
                
        
        return k