class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic Programming approach
        rob1, rob2 = 0, 0
        for n in nums:
            current = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = current
        
        return rob2