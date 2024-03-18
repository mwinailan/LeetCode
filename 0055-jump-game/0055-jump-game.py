class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate through all num from behind
        reachable = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # move the reachable pointer if appropriate
            if (nums[i] + i) >= reachable:
                reachable = i
        
        return reachable == 0