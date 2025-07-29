class Solution:
    # Time: O(1) / Space: O(1)
    def findClosest(self, x: int, y: int, z: int) -> int:
        if x == y: return 0
        if abs(z - x) == abs(z - y):
            return 0
        if abs(z - x) < abs(z - y):
            return 1
        else:
            return 2
