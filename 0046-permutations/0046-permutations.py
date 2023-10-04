class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            val = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(val)
            
            nums.append(val)
            res.extend(perms)
        return res
        