/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {

        // Collections.sort(intervals, Comparator.comparingInt(i -> i.start));
        
        // // Compare the current end <= next start
        // for (int i = 0; i < intervals.size() - 1; i++) {
        //     Interval current = intervals.get(i);
        //     Interval next = intervals.get(i + 1);
        //     if (current.end > next.start) {
        //         return false;
        //     }
        // }
        // return true;



        // Is the List sorted? No
        // 1. sort the List
        Collections.sort(intervals, Comparator.comparingInt(i -> i.start));

        // for loop to check if (interval[i][end] < interval[i + 1][start])
        for (int i = 0; i < intervals.size() - 1; i++) {
            Interval cur = intervals.get(i);
            Interval next = intervals.get(i+1);
            if (cur.end > next.start)
                return false;
        }
        return true;
    }
}
