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
        ## sort with the start time
        intervals.sort(key=lambda i: i.start)

        ## compare prev_end with cur_start
        prev_end = intervals[0].end


        for i in range(1, len(intervals)):
            cur_start = intervals[i].start
            print (f"Prev End: {prev_end}")
            print (f"Cur Start: {cur_start}")

            if cur_start < prev_end:
                # if conflict
                return False

            prev_end = intervals[i].end

        return True 
