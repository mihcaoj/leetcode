'''
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1.
Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.
As the town detective, your task is to find these two sneaky numbers.
Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
'''
class Solution:
    # Time: O(n) / Space: O(n)
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky_numbers = []
        counter = Counter(nums)

        for key in counter:
            if counter[key] > 1:
                sneaky_numbers.append(key)
        return sneaky_numbers
