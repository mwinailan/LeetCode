class Solution:
    def rob(self, nums: List[int]) -> int:
        #house_a house_b current_house
        house_a = 0
        house_b = 0
        max_profit = 0
        for i in range(len(nums)):
            current_house = max(nums[i] + house_a, house_b, nums[i])
            max_profit = max(max_profit, current_house)
            house_a = house_b
            house_b = current_house
        
        return max_profit
        