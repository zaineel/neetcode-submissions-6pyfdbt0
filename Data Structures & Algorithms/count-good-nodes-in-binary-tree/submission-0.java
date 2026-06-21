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
    public int goodNodes(TreeNode root) {
      return dfs(root, Integer.MIN_VALUE);
  }
  private int dfs(TreeNode node, int maxSeenSoFar){
    if (node == null){
      return 0;
    }
    int count = node.val >= maxSeenSoFar ? 1 : 0;
    int updatedMax = Math.max(maxSeenSoFar, node.val);

    count += dfs(node.left, updatedMax);
    count += dfs(node.right, updatedMax);

    return count;
  }
}
