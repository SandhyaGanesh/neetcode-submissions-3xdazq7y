"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervalTuples = [(i.start, i.end) for i in intervals]
        intervalTuples.sort()
        prevEnd = intervalTuples[0][1]
        for start, end in intervalTuples[1:]:
            if start < prevEnd:
                return False
            prevEnd = end
        return True