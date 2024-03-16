class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn) time complexity overall because of sorting
        intervals.sort()
        removedIntervals = 0
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # Case 1: start time of current interval is more than the previous end time interval
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            # Case 2: else, find the time of the interval that ends first, and remove one of them
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                removedIntervals += 1
                
        return removedIntervals
        
        