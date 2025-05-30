class Solution:
    # Time: O(n) / Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        my_set = set(nums)

        for i in range(0, n):
            if i not in my_set:
                return i
