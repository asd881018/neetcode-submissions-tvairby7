class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 1------3
        #     2------5
        #                 6---------------7

        # 1----------5    6 --------------7

        # O(nlogn)

        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:

            # overlapping
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)

            else:
                output.append([start, end])

        return output

