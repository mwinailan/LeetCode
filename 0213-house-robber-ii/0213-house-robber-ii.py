class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(houses):
            neighborHouse = 0
            houseOneOver = 0
            maxMoney = 0
            for house in houses:
                maxMoney = max(house + houseOneOver, neighborHouse)
                houseOneOver = neighborHouse
                neighborHouse = maxMoney
            return maxMoney
                
        return max(houseRobber(nums[1:]), houseRobber(nums[:-1]), nums[0])
            