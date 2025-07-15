'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank.
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
'''
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
