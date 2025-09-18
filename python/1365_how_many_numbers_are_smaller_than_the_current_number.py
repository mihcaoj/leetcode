# Time: O(nlogn) / Space: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        dictionary = {}
        result = []

        for i, num in enumerate(sorted_nums):
            if num not in dictionary:
                dictionary[num] = i

        for i in nums:
            result.append(dictionary[i])

        return result
