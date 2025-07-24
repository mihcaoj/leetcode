'''
You are given an integer array nums.
The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.
'''
class Solution:
    # Time: O(n) / Space: O(n)
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum([k for k, v in count.items() if v == 1])
