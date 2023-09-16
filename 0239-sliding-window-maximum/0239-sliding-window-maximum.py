class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        left = right = 0
        maxRes = []
        
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                maxRes.append(nums[queue[0]])
                left += 1
            
            right += 1
        
        return maxRes