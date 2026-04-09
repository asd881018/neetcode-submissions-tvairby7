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


        // size range of the intervals? 
        // is the intervals sorted?
        // is the value of start and end all positive?
        // is start < end?

        // 1. Sort the List
        Collections.sort(intervals, Comparator.comparingInt(i-> i.start));


        // 2. Use for loop to find if (cur.end <= next.start)

        for (int i = 0; i < intervals.size() - 1; i++) {
            Interval cur = intervals.get(i);
            Interval next = intervals.get(i+1);
            if (cur.end > next.start){
                return false;
            }
        }
        return true;
    }
}
