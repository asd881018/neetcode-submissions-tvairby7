# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1,2,3,4.....100....m-1, m]
        # remove (m - n + 1)
        # how to get the length? traverse all the nodes and count

        # reverse the list then remove the n
        # then  reverse back

        # if we have l, r pointers
        # keep r - l = n
        # when r = null, l = the node we need to remove

        dummy = ListNode(0, head) 
        l, r = dummy, head
        cur = head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        prev = l
        next = l.next.next
        
        l.next = None
        prev.next = next

        return dummy.next


        