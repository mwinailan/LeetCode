class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        intervalList = [intervals[0]]
        for i in range(len(intervals)):
            if intervalList[-1][1] >= intervals[i][0]:
                intervalList[-1][1] = max(intervalList[-1][1], intervals[i][1])
            else:
                intervalList.append(intervals[i])
        
        return intervalList
        