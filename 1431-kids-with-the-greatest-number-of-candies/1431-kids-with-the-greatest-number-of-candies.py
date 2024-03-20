class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_with_most_candies = max(candies)
        result = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= kid_with_most_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
        