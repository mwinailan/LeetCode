class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicatePile = set()
        for n in nums:
            if n in duplicatePile:
                return True
            duplicatePile.add(n)
        
        return False
        