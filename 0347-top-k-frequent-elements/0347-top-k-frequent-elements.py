class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfNums = [[] for i in range(len(nums) + 1)]
        letterCounts = {}
        result = []
        
        for n in nums:
            letterCounts[n] = 1 + letterCounts.get(n, 0)
        
        for n, count in letterCounts.items():
            print(n, count)
            countOfNums[count].append(n)
    
        for i in range(len(nums), 0, -1):
            for element in countOfNums[i]:
                result.append(element)
                if len(result) == k:
                    return result
            