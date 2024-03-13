class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervalResult = []
        for i in range(len(intervals)):
            # Case 1: interval end before newInterval start
            if intervals[i][1] < newInterval[0]:
                intervalResult.append(intervals[i])
            # Case 2: newInterval end before interval start
            elif newInterval[1] < intervals[i][0]:
                intervalResult.append(newInterval)
                return intervalResult + intervals[i:]
            # Case 3: overlapping intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        intervalResult.append(newInterval)
        
        return intervalResult