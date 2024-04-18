class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        for n in nums:
            number_count[n] = 1 + number_count.get(n, 0)
        
        count_frequency = [[] for _ in range(len(nums) + 1)]
        for number, count in number_count.items():
            count_frequency[count].append(number)
        
        top_k_frequent = []
        for i in range(len(count_frequency) - 1, -1, -1):
            for n in count_frequency[i]:
                top_k_frequent.append(n)
                if len(top_k_frequent) == k:
                    return top_k_frequent
                
        return top_k_frequent
                
            
        
        