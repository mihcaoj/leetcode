class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// Time: O(n) / Space: O(n)
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const result = [];
  const queue = [root];

  while (queue.length > 0) {
    let n = queue.length;
    let newLevel = [];
    for (let i = 0; i < n; i++) {
      let node = queue.shift()!;
      newLevel.push(node.val);

      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
    }
    result.push(newLevel);
  }
  return result;
}
