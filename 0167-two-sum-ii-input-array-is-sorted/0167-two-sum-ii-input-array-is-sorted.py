class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1
        
        while (leftPointer < rightPointer):
            total = numbers[leftPointer] + numbers[rightPointer]
            if total > target:
                rightPointer -= 1
            elif total < target:
                leftPointer += 1
            else:
                return [leftPointer + 1, rightPointer + 1]
            
            
        