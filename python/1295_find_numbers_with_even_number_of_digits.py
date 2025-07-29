class Solution:
    # Time: O(n) / Space: O(1)
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for i in range(0, len(nums)):
            s = str(nums[i])
            if len(s) % 2 == 0:
                even_count += 1
        return even_count
