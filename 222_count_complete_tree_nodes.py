class Solution:
    # Recursive DFS - Naive solution (Time: O(n) / Space: O(h))
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Optimal solution (Time: O(log^2 n) / Space: O(log n))
    def countNodes(self, root, l=1, r=1):
        if not root: return 0
        left = right = root
        while left  := left.left: l += 1
        while right := right.right: r += 1

        # If tree is complete (2^depth - 1)
        if l == r: return 2**l - 1

        # If the tree is incomplete, recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
