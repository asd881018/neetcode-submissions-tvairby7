# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # map(dict) record the whole list with index

        seen = {}
        i = 0
        cur = head

        while cur:
            seen[i] = cur
            i+=1
            cur = cur.next
        
        # we got the record with index

        # we want to remove n from the end
        # The actual target index to remove is (lens(seen) - n)

        targetIndex = len(seen) - n
        targetNode = seen[targetIndex]

        # change the next of the prev to cur.next
        # prevIndex = targetIndex - 1
        
        if targetIndex == 0:
            return head.next
        
        prev = seen[targetIndex - 1]
        prev.next = targetNode.next

        return head
        

        