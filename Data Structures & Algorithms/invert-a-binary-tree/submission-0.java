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
    public TreeNode invertTree(TreeNode root) {
        // Create another TreeNode and having the opposite left and right node
        // Traverse the tree, append the origial node with opposite left and right to the new tree

        if (root == null){
            return null;
        }
        
        TreeNode newRoot = new TreeNode(root.val);
        
        newRoot.right = invertTree(root.left);
        newRoot.left = invertTree(root.right);

        return newRoot;
    }
}
