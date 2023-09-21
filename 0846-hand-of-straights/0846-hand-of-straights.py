class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = {}
        for n in hand:
            cardCount[n] = 1 + cardCount.get(n, 0)
        
        minStack = list(cardCount.keys())
        heapq.heapify(minStack)
        
        while minStack:
            for i in range(minStack[0], minStack[0] + groupSize):
                if i not in cardCount:
                    return False
                cardCount[i] -= 1
                if cardCount[i] == 0:
                    if minStack[0] != i:
                        return False
                    heapq.heappop(minStack)
        
        return True
                    
        