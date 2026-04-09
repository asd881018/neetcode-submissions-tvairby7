/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Traverse two tree at the same time, and check if each value the same
        
        if ((p == null && q != null) || (q == null && p != null)) {
            return false;
        }

        if (p == null && q == null) {
            return true;
        }
        
        if (p.val != q.val) {
            return false;
        }

        boolean left = isSameTree(p.left, q.left);
        if (left == false){
            return false;
        }
        boolean right = isSameTree(p.right, q.right);
        if (right == false){
            return false;
        }


        return true;
    }
}
