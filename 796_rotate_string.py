class Solution:
    # Time: O(n) / Space: O(n)
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        return goal in s + s
