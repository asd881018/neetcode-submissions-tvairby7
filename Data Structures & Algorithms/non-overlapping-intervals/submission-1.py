class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # check overlapping (a.end > b.start)
        # remove the one with longer end

        intervals.sort(key=lambda i:i[0])

        compareEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:

            if compareEnd > start:
                count += 1
                compareEnd = min(compareEnd, end)
                continue
            
            compareEnd = end
        
        return count

