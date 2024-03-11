class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArray = [0] * (len(nums))
        # Calculate prefix and postfix for nums. Do 2 passes on nums array
        prefix = 1
        for i in range(len(nums)):
            productArray[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            productArray[i] *= postfix
            postfix *= nums[i]
        
        return productArray
            