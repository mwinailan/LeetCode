class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalpost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= goalpost:
                goalpost = i
        
        if goalpost == 0:
            return True
        else:
            return False