class Solution:
    # Time: O(n) / Space: O(n)
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky_numbers = []
        counter = Counter(nums)

        for key in counter:
            if counter[key] > 1:
                sneaky_numbers.append(key)
        return sneaky_numbers
