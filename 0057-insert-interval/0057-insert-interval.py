class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                newIntervals.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(intervals[i][1], newInterval[1])]
            
        newIntervals.append(newInterval)
        
        return newIntervals
        