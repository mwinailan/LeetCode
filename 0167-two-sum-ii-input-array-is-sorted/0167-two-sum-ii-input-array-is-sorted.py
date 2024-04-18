class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointer solution
        # O(1) space
        # O(n) time
        
        left, right = 0, len(numbers) - 1
        
        while(left < right):
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
        