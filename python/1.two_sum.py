class Solution:
    # Naive solution (Time: O(n^2) / Space: O(n^2))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Optimal solution (Time: O(n) / Space: O(n))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
