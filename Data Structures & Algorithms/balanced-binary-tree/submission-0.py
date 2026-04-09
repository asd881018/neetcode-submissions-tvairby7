# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root):
            if not root:
                return [True, 0]

            # left and right

            left = dfs(root.left)
            right = dfs(root.right)

            isBalanced = True

            if (abs(left[1] - right[1]) > 1 or left[0] != True or right[0] != True):
                isBalanced = False
            
            return [isBalanced, max(left[1], right[1]) + 1]

        return dfs(root)[0]
