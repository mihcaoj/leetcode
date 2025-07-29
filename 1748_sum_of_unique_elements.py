class Solution:
    # Time: O(n) / Space: O(n)
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum([k for k, v in count.items() if v == 1])
