'''
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''
class Solution:
    # Time: O(n + logk) / Space: O(n + logk)
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in reversed(range(len(num))):
            total = num[i] + k
            num[i] = total % 10
            k = total // 10
        while k:
            digit = k % 10
            num = [digit] + num
            k = k // 10
        return num
