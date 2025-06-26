'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
class Solution:
    # Time: O(n) / Space: O(h)
    def is_mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left and right:
            return (left.val == right.val and
                self.is_mirror(left.left, right.right) and
                self.is_mirror(left.right, right.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
