class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberContainer = set()
        
        for n in nums:
            numberContainer.add(n)
        
        if len(nums) != len(numberContainer):
            return True
        else:
            return False
        