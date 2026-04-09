"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1:
            return True

        # sort the interval by start time
        intervals.sort(key=lambda interval: interval.start)

        # return false if prev.end > cur.start
        prev = intervals[0]

        for i in range(1, len(intervals)):
            cur = intervals[i]

            if (prev.end > cur.start):
                return False

            prev = cur

        return True
        
