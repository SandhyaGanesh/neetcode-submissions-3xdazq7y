"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetingRooms = {}
        meetingTimes = []
        for interval in intervals:
            meetingRooms[interval.start] = meetingRooms.get(interval.start, 0) + 1
            meetingRooms[interval.end] = meetingRooms.get(interval.end, 0) - 1
            meetingTimes.append(interval.start)
            meetingTimes.append(interval.end) 
        meetingTimes = list(set(meetingTimes))
        meetingTimes.sort()

        maxRooms = 0
        rooms = 0
        for meetingTime in meetingTimes:
            rooms += meetingRooms[meetingTime]
            maxRooms = max(rooms, maxRooms)
        return maxRooms