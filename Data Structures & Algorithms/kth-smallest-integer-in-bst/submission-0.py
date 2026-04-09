# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack:
            while cur:
                # Keep going left
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1

            if k == 0:
                return cur.val

            ## Go to right node
            cur = cur.right

        return root.val

        
