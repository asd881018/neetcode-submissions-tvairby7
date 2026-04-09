/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        // ListNode current = head;
        // ListNode previous = null;
        // ListNode nextCurrent = null;

        // while (current != null){
        //     nextCurrent = current.next;
        //     current.next = previous;
        //     previous = current;
        //     current = nextCurrent;
        // }

        // return previous;

        // 1 -> 2 -> 3 -> 4 -> 5 -> null

        // null <- 1 <- 2 <- 3 <- 4 <- 5

        ListNode cur = head;
        ListNode next = null;
        ListNode prev = null;

        while(cur != null){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }
}
