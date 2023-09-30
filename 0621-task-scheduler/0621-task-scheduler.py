class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = collections.deque()
        taskCount = Counter(tasks)
        maxHeap = [-count for count in taskCount.values()]
        timeStamp = 0
        heapq.heapify(maxHeap)
        while maxHeap or queue:
            timeStamp += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, timeStamp + n])
            
            if queue and queue[0][1] == timeStamp:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return timeStamp