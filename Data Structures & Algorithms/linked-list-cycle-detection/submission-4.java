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
    public boolean hasCycle(ListNode head) {
        // Find if there's no null node for any node.next
        // if we have node 5 not in the loop, then this solution does not work

        // Create a HashMap to reocrd the count and node (maybe location?). 
        // Traverse the list, and see if we if any count > 1

        // if (head == null)
        //     return false;

        // ListNode current = head;
        // HashMap <ListNode, Integer> map = new HashMap<>();

        // while(current != null){
        //     if (map.containsKey(current)){
        //         return true;
        //     }
        //     map.put(current, map.getOrDefault(current, 0) + 1);
        //     current = current.next;
        // } 
        // return false;

        // // Use a slow (next) and fast (next.next)
        // // If fast meet null, then it has no loop
        // // If if fast and slow meet, means it has loop
        // ListNode slow = head;
        // ListNode fast = head;

        // while (fast!=null && fast.next!=null) {
        //     slow = slow.next;
        //     fast = fast.next.next;

        //     if (slow == fast){
        //         return true;
        //     }      
        // }
        // return false;


        // Use a HashMap to record all the nodes traversed
        // Map <ListNode, Integer> map = new HashMap<>();
        // ListNode cur = head;

        // // Check if there's any same node
        // while(cur != null){
        //     if (map.containsKey(cur)){
        //         return true;
        //     }
        //     map.put(cur, map.getOrDefault(cur, 0) + 1);
        //     cur = cur.next;
        // }
        // return false;


        
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
}
