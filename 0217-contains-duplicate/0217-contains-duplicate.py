class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        
        for n in nums:
            if n in contains:
                return True
            contains.add(n)
            
        return False