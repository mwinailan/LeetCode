class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return None
        nums.sort()
        
        threeSumResult = []
        
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Find j and k with a 2 pointer solution
            while j < k:
                totalSum = nums[i] + nums[j] + nums[k]
                # Case 1: totalsum is larger than 0, move k by 1 to the left
                if totalSum > 0:
                    k -= 1
                # Case 2: totalsum is smaller than 0, move j by 1 to the right
                elif totalSum < 0:
                    j += 1
                # Case 3: totalsum is 0, add to the threeSumResult, and move j pointer
                else:        
                    threeSumResult.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        
        return threeSumResult
