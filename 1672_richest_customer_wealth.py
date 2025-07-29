class Solution:
    # Time: O(n) / Space: O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        summ, max_wealth = 0, 0

        for account in accounts:
            summ = sum(account)
            if summ > max_wealth:
                max_wealth = summ
        return max_wealth

    # One-liner (Time: O(n) / Space: O(n))
    def maximumWealth(self, accounts: List[List[int]]) -> int:
            return max([sum(account) for account in accounts])
