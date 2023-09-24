class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTriplet = set()
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i, value in enumerate(t):
                    if value == target[i]:
                        validTriplet.add(i)
        
        if len(validTriplet) == 3:
            return True
        else:
            return False