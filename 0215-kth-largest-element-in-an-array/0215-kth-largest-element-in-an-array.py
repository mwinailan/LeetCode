class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-c for c in nums]
        heapq.heapify(maxHeap)
        
        while maxHeap and k > 0:
            res = heapq.heappop(maxHeap)
            res = -res
            k -= 1
        
        return res
            