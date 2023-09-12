class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        alreadyExists = set()
        
        for n in nums:
            if n in alreadyExists:
                return True
            alreadyExists.add(n)
        
        return False
        