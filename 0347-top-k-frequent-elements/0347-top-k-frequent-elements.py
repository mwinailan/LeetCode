class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Have the count of each num as an index
        frequency = [[] for i in range(len(nums) + 1)]
        letterCount = {}
        
        # Count each num in nums
        for num in nums:
            letterCount[num] = 1 + letterCount.get(num, 0)
        
        # Put the letter counts into the frequency array
        for num, count in letterCount.items():
            frequency[count].append(num)
        
        # Get the top k frequent elements
        topKFrequent = []
        for i in range(len(nums), -1, -1):
            for n in frequency[i]:
                topKFrequent.append(n)
                
                if len(topKFrequent) == k:
                    return topKFrequent
            
        