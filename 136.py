class Solution:
    # Naive solution
    def singleNumber(self, nums: List[int]) -> int:
        my_set = set()

        for i in range(len(nums)):
            if nums[i] not in my_set:
                my_set.add(nums[i])
            else:
                my_set.remove(nums[i])
        return my_set.pop()

    # Optimal solution
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = n ^ result
        return result
