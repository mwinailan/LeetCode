class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def validate(threshold):
            i, count = 0, 0
            
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p :
                    return True    
                
            return False
       

        if p == 0:
            return 0
        
        nums.sort()
        l, r = 0, nums[len(nums)-1]
        res = nums[len(nums)-1]
        while l <= r:
            mid = l + (r - l) // 2
            if validate(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        