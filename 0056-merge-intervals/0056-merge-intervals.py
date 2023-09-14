class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda intervals : intervals[0])
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            prevStart, prevEnd = res[-1][0], res[-1][1]
            currentStart, currentEnd = interval[0], interval[1]
            
            if currentStart <= prevEnd:
                res[-1][0] = min(prevStart, currentStart)
                res[-1][1] = max(currentEnd, prevEnd)           
            else:
                res.append(interval)
            
        
        return res
        