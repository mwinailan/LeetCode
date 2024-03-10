class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums) + 1)]
        elementToCount = {}
        
        for n in nums:
            elementToCount[n] = 1 + elementToCount.get(n, 0)
        
        for element, count in elementToCount.items():
            frequency[count].append(element)
        
        topKFrequent = []
        for i in range(len(frequency) - 1, 0, -1):
            for e in frequency[i]:
                topKFrequent.append(e)
                if len(topKFrequent) == k:
                    return topKFrequent
        
        return topKFrequent
        