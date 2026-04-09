# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = ListNode()
        cur = newList
        cur1, cur2 = list1, list2
        ## while list 1 and 2 are not empty
        while cur1 and cur2:
            ## compare the the cur1 and cur2's value
            ## put the smaller one into the newList
            ## then traverse to the next node
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            
            else:
                cur.next = cur2
                cur2 = cur2.next

            cur = cur.next  
                    
        ## After while loop
        ## Handle the node left eithier from list1 or list2

        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        
        return newList.next