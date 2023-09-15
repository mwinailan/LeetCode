class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervalsRemoved = 0
        intervals.sort(key=lambda intervals : intervals[0])
        prevEnd = intervals[0][1]
        
        for currentStart, currentEnd in intervals[1:]:
            if currentStart >= prevEnd:
                prevEnd = currentEnd
            else:
                prevEnd = min(prevEnd, currentEnd)
                intervalsRemoved += 1
        
        return intervalsRemoved
        
        