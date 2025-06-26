'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.
'''
class Solution:
    # Time: O(2^n) / Space: O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        solution = []
        results = []

        def backtrack(i):
            # Base case
            if i == n:
                results.append(solution[:]) # append a copy of the solution
                return

            # Don't pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            solution.append(nums[i])
            backtrack(i + 1)
            solution.pop()

        backtrack(0)
        return results
