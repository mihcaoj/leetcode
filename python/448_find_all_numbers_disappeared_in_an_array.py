class Solution:
    # Time: O(n) / Space: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [i + 1 for i in range(n) if nums[i] != i + 1]
