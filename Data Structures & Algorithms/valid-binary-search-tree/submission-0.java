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
                            2
                    /             \   
                  1                 3  
                                /        \ 
                               1           4
psudocode
1. create dfs helper func
2. if node is null -> true
3. base case: if lower is not null and node.val <= lower, return false
4. base case: if upper is not null and node.val >= upper, return false
5. recursion begins:
a. check left hand side with range of (lower, node.val)
b. check right hand side with ragnge(node.val, upper)
return true only if both left and right are valid

 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, null, null);
    }
    private boolean dfs(TreeNode root, Long lower, Long upper){
        if(root == null){
            return true;
        }
        // base case
        if (lower != null && root.val <= lower){
            return false;
        }
        if (upper != null && root.val >= upper){
            return false;
        }
        return dfs(root.left, lower, (long)(root.val)) && dfs(root.right, (long)(root.val), upper);
    }




















}
