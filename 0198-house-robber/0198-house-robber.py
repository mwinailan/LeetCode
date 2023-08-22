class Solution:
    def rob(self, nums: List[int]) -> int:   
        houseOverMaxMoney = 0
        maxMoney = 0
        houseIndex = 0
        
        while(houseIndex < len(nums)):
            currentMoney = max(nums[houseIndex] + houseOverMaxMoney, maxMoney)
            houseOverMaxMoney = maxMoney
            maxMoney = currentMoney
            houseIndex += 1
        
        return maxMoney
            
            
            
            