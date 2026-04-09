# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # cycle: when traversing, we meet the previous node met before

        # 1. having a map to store the node, then every time we travers
        # the next node, we check if it is in the map
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next

        
        return False


        # 2. slow and fast index to traverse
        # slow: move 1 node
        # fast: move 2 node

        # if not head or not head.next:
        #     return False

        # slow, fast = head, head.next 

        # while fast and fast.next:
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        
        # return False