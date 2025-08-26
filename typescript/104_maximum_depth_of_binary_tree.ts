// Time: O(n) / Space: O(n)
function maxDepth(root: TreeNode | null): number {
  function dfs(root: TreeNode | null): number {
    if (!root) return 0;
    return Math.max(dfs(root.left), dfs(root.right)) + 1;
  }

  if (root) {
    return dfs(root);
  } else {
    return 0;
  }
}
