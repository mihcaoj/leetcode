class Solution:
    # Recursive solution (Time: O(2^n) / Space: O(n))
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    # Iterative solution (Time: O(n) / Space: O(1))
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    # Memoization solution (Time: O(n) / Space: O(n))
    def fib(self, n: int) -> int:
        memo = {}

        def dp(k):
            if k == 0: return 0
            if k == 1: return 1
            if k in memo: return memo[k]

            memo[k] = dp(k - 1) + dp(k - 2)
            return memo[k]

        return dp(n)
