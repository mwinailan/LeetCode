class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        startingIndex = 0
        totalRange = 0
        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            totalRange += difference
            
            if totalRange < 0:
                totalRange = 0
                startingIndex = i + 1
        
        return startingIndex
        