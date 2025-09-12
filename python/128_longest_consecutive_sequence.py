# Time: O(n) / Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0

        for num in my_set:
            if num - 1 not in my_set:
                length = 1
                while num + length in my_set:
                    length += 1
                longest = max(longest, length)

        return longest
