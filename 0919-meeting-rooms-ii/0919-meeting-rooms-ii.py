from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        startTimes, endTimes = [], []
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()
        s, e = 0, 0
        minMeetingRooms, currentMeetingRooms = 0, 0
        while s < len(intervals):
            if startTimes[s] < endTimes[e]:
                currentMeetingRooms += 1
                s += 1
            else:
                currentMeetingRooms -= 1
                e += 1
            minMeetingRooms = max(minMeetingRooms, currentMeetingRooms)
        
        return minMeetingRooms
