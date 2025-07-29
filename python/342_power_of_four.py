class Solution:
    # Time: O(logn) / Space: O(1)
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False

        while n % 4 == 0:
            n //= 4
        return n == 1
