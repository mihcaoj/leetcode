'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
'''
class Solution:
    # Time: O(n) / Space: O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())
