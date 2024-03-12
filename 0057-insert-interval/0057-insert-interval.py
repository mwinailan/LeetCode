class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        for i in range(len(intervals)):
            # Case 1: newInterval starts after cEnd
            if newInterval[0] > intervals[i][1]:
                newIntervals.append(intervals[i])
            # Case 2: newInterval ends before cStart
            elif newInterval[1] < intervals[i][0]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            # Case 3: newInterval overlaps the previous interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        newIntervals.append(newInterval)
        return newIntervals
            