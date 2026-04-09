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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

        // if (subRoot == null) {
        //     return true;
        // }

        // if (root == null) {
        //     return false;
        // }

        // if (isSame(root, subRoot)) {
        //     return true;
        // }

        // return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));


        // Use recursive

        // Base case:
        if (subRoot == null) {
            return true;
        }

        if (root == null) {
            return false;
        }

        // Check if it is the same tree
        if (isSame(root, subRoot)) {return true;}

        // Check if left or right of root is the subroot or not
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

     public boolean isSame(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {return true;}
        if (root != null && subRoot != null && root.val == subRoot.val) {
            return isSame(root.left, subRoot.left) && isSame(root.right, subRoot.right);
        }
        return false;
     }

//     public boolean isSame(TreeNode root, TreeNode subRoot){
//         if (root == null && subRoot == null) {
//             return true;
//         }

//         if (root != null && subRoot != null && root.val == subRoot.val){
//             return isSame(root.left, subRoot.left) && isSame(root.right, subRoot.right);
//         }
//         return false;
//     }
}
