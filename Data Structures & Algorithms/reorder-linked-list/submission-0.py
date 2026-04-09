# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head = [2,4,6,8,10]
        # head = [2,4,6,8]
        #           s   f

        # split the first half and second half
        # slow and fast pointer
        # second = s.next is the start of the fast pointer
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        prev = s.next = None

        # reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # traverse node in 1st half, then 2nd half...
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2


        



        