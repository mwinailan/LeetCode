class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        #linear solution
        for n in nums:
            if n == res:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                count = 0
                res = n
        
        return res