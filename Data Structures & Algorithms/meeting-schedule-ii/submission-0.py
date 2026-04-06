"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        tim = [0]*1000001
        for interval in intervals:
            for t in range(interval.start, interval.end):
                tim[t] += 1
        return max(tim)