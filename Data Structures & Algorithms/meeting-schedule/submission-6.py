"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i : i.start)
        
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            start = interval.start
            prev_end = intervals[i - 1].end
            if start < prev_end:
                return False

        return True

            
