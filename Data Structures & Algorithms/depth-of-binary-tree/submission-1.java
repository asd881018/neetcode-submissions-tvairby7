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
    public int maxDepth(TreeNode root) {
        // Use recursion
        // base case: 1
        // if (root == null){
        //     return 0;
        // }
        
        // TreeNode left = root.left;
        // TreeNode right = root.right;

        // int leftDepth = maxDepth(left) + 1;
        // int rightDepth = maxDepth(right) + 1;

        // return Math.max(leftDepth, rightDepth);



        // Use recursive for left and right
        // base case: root == null, return 0
        if (root == null) { return 0; }
        TreeNode left = root.left;
        TreeNode right = root.right;


        int leftDepth = maxDepth(left) + 1;
        int rightDepth = maxDepth(right) + 1;

        // find the max the number of left and right 
        return Math.max(leftDepth, rightDepth);

        // return the max value

    }
}
