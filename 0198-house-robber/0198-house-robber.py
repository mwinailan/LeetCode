class Solution:
    def rob(self, nums: List[int]) -> int:
        # house1   house2  curhouse
        house1, house2 = 0, 0
        # DP solution
        for n in nums:
            curhouse = max(n + house1, house2)
            house1 = house2
            house2 = curhouse
        
        return house2