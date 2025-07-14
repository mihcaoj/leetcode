'''
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''
class Solution:
    # Naive solution (Time: O(n^2) / Space: O(1))
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs += 1
        return good_pairs

    # Better solution (Time: O(n) / Space: O(n))
    def numIdenticalPairs(self, nums: List[int]) -> int:
            good_pairs = {}
            count = 0

            for i in range(len(nums)):
                if nums[i] in good_pairs:
                    count += good_pairs[nums[i]]
                good_pairs[nums[i]] = good_pairs.get(nums[i], 0) + 1
            return count
