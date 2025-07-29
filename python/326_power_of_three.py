class Solution:
    # Time: O(logn) / Space: O(1)
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False

        while n % 3 == 0:
            n //= 3
        return n == 1
