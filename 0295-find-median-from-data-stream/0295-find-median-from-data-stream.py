class MedianFinder:

    def __init__(self):
        self.smallHeap, self.bigHeap = [], [] #smallHeap is maxHeap, bigHeap is minHeap        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)
        
        if self.smallHeap and self.bigHeap and (-1 * self.smallHeap[0]) > self.bigHeap[0]:
            tempNum = heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, -1 * tempNum)
        
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            tempNum = heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, -1 * tempNum)
        
        if len(self.bigHeap) > len(self.smallHeap) + 1:
            tempNum = heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, -1 * tempNum)
        

    def findMedian(self) -> float:
        if (len(self.smallHeap) + len(self.bigHeap)) % 2 == 1:
            if len(self.smallHeap) > len(self.bigHeap):
                return -1 * self.smallHeap[0]
            else:
                return self.bigHeap[0]
        else:
            return ((-1 * self.smallHeap[0]) + self.bigHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()