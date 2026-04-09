# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            
            val = node.val
            
            if not (val > left and val < right):
                return False

            return valid(node.left, left, val) and valid(node.right, val, right)

        return valid(root, float("-inf"), float("inf"))