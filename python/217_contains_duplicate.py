class Solution:
    # Set solution (Time: O(n) / Space: O(n))
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False

    # Sort solution (Time: O(nlogn) / Space: O(1))
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
