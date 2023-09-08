class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        adjustedIntervals = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                adjustedIntervals.append(newInterval)
                return adjustedIntervals + intervals[i:]
            elif newInterval[0] > interval[1]:
                adjustedIntervals.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        adjustedIntervals.append(newInterval)
        return adjustedIntervals