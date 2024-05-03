class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        new_intervals = [intervals[0]]
        
        for interval in intervals:
            if new_intervals[-1][1] >= interval[0]:
                new_intervals[-1][1] = max(new_intervals[-1][1], interval[1])
            else:
                new_intervals.append(interval)
        
        return new_intervals