class Solution:
    # Naive solution (Time: O(nlogn) / Space: O(n))
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0

        for i in range(len(nums)):
            square = nums[i] ** 2
            nums[i] = square

        nums.sort()
        return nums

    # More efficient solution (Time: O(n) / Space: O(n))
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l, r = 0, len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
        return result
