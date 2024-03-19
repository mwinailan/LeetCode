class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = 0
        min_swaps = float("Inf")
        # count number of 1's
        for n in data:
            if n == 1:
                ones_count += 1
        
        if ones_count == 1:
            return 0
        
        # create subarrays of size of number of 1's, and count the amount of zeroes
        left = 0
        zeroes_count = 0
        for right in range(len(data)):
            if data[right] == 0:
                zeroes_count += 1
            
            if (right - left + 1) == ones_count:
                min_swaps = min(min_swaps, zeroes_count)
                if data[left] == 0:
                    zeroes_count -= 1
                left += 1

        return 0 if min_swaps == float("Inf") else min_swaps
                
            