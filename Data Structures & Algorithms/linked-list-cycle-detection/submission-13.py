# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # l moves 1 step, r moves 2 steps
        # 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2
   
        #           l              r

        l, r = head, head

        while r and r.next:
            l = l.next
            r = r.next.next

            if l == r:
                return True

        return False

        