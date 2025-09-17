# Time: O(logn) / Space: O(logn)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False  # cycle
            seen.add(n)
            digits = [int(d) for d in str(n)]
            sum_of_squares = sum(digit**2 for digit in digits)
            n = sum_of_squares

        return True
